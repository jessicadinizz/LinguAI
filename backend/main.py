from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from typing import List
from openai import OpenAI
import os

from database import Base, engine, SessionLocal
import models, schemas, auth

# Load variáveis do .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Cria tabelas do banco
Base.metadata.create_all(bind=engine)

# Inicializa app
app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Header opcional p/ documentação (não usado de fato)
oauth2_scheme = APIKeyHeader(name="Authorization", auto_error=False)


# Conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Autenticação a partir do token
def usuario_autenticado(request: Request, db: Session = Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token ausente ou mal formatado")

    token = auth_header.split(" ")[1]
    user_id = auth.verificar_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Token inválido")

    user = db.query(models.User).filter_by(id=int(user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user


# --------- ROTAS ---------


@app.post("/register")
def register(dados: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter_by(email=dados.email).first():
        raise HTTPException(status_code=400, detail="Usuário já existe")
    novo = models.User(email=dados.email, senha_hash=auth.hash_senha(dados.senha))
    db.add(novo)
    db.commit()
    return {"msg": "Usuário criado com sucesso"}


@app.post("/login")
def login(dados: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(email=dados.email).first()
    if not user or not auth.verificar_senha(dados.senha, user.senha_hash):
        raise HTTPException(status_code=401, detail="Login inválido")
    token = auth.criar_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/atividades", response_model=schemas.AtividadeOut)
def salvar_atividade(
    data: schemas.AtividadeBase,
    user=Depends(usuario_autenticado),
    db: Session = Depends(get_db),
):
    nova = models.Atividade(**data.dict(), user_id=user.id)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@app.get("/atividades", response_model=List[schemas.AtividadeOut])
def listar_atividades(user=Depends(usuario_autenticado), db: Session = Depends(get_db)):
    atividades = db.query(models.Atividade).filter_by(user_id=user.id).all()
    return atividades


@app.get("/teste-token")
def teste_token(token: str):
    user_id = auth.verificar_token(token)
    return {"user_id": user_id}


# --------- IA: GERAÇÃO DE FLASHCARDS E QUIZ ---------


class TextoEntrada(BaseModel):
    texto: str


@app.post("/gerar-flashcards")
async def gerar_flashcards(dados: TextoEntrada):
    prompt = f"""
Você é um assistente de ensino de inglês. Abaixo está um texto.

Extraia exatamente 5 palavras ou expressões úteis e forneça:
- Palavra (em inglês)
- Tradução em português
- Exemplo de uso (em inglês)

Formato:
FLASHCARDS:
- Palavra | Tradução | Exemplo em inglês

Texto:
\"\"\"{dados.texto}\"\"\"
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o", messages=[{"role": "user", "content": prompt}]
        )
        return {"conteudo": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/gerar-quiz")
async def gerar_quiz(dados: TextoEntrada):
    prompt = f"""
Você é um assistente de ensino de inglês. Abaixo está um texto de referência.

Sua tarefa é gerar 3 perguntas de múltipla escolha focadas em vocabulário e gramática do inglês, com base nas palavras ou expressões usadas no texto.

🧩 Cada pergunta deve:
- Testar o significado ou uso correto de palavras/frases do texto.
- Cobrar o uso correto em frases, sinônimos, preposições, tempos verbais ou collocations.
- Ter 4 alternativas (a-d), plausíveis e diferentes.
- Ter apenas uma correta.
- Ser clara, objetiva e útil para o aprendizado da língua inglesa.

📌 NÃO faça perguntas de interpretação do texto.  
📌 NÃO copie frases do texto.  
📌 NÃO inclua explicações nem traduções.

📝 Formato obrigatório da resposta:
QUIZ:
1. Pergunta?
   a) ...
   b) ...
   c) ...
   d) ...
Resposta correta: letra x)

Texto de referência:
\"\"\"{dados.texto}\"\"\"
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o", messages=[{"role": "user", "content": prompt}]
        )
        return {"conteudo": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
