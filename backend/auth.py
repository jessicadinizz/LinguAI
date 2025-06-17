from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from database import SessionLocal
from models import User

# Configurações do token
SECRET_KEY = "segredo-super-seguro"  # pode colocar isso no .env
ALGORITHM = "HS256"
EXPIRA_MIN = 30

# Criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Autenticação via token OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Gerar hash da senha
def hash_senha(senha: str):
    return pwd_context.hash(senha)


# Verificar senha com hash
def verificar_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)


# Criar token JWT
def criar_token(dados: dict):
    to_encode = dados.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRA_MIN)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Decodificar token e extrair ID do usuário
def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")  # deve ser o user.id
    except JWTError:
        return None


# Dependência para obter o usuário atual a partir do token
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    user_id = verificar_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user
