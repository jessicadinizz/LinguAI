````markdown
# TCC - Sistema de Aprendizado de Inglês com IA

Este é um projeto de TCC que visa desenvolver uma plataforma para aprendizado de inglês com o uso de inteligência artificial. A plataforma permite que o usuário envie textos, os quais são processados para gerar flashcards e quizzes, facilitando o aprendizado do vocabulário e gramática da língua inglesa.

## Descrição

O **backend** do projeto foi desenvolvido utilizando **FastAPI**, **SQLAlchemy**, e **OpenAI** para gerar flashcards e quizzes baseados em textos enviados pelos usuários. O sistema permite que os usuários se registrem, façam login e gerenciem suas atividades de aprendizado.

### Funcionalidades principais:
- **Autenticação de usuários** com tokens JWT.
- **Criação de atividades de aprendizado**, onde os usuários podem enviar textos e gerar flashcards e quizzes.
- **Geração de Flashcards** usando IA, extraindo palavras/expressões úteis dos textos.
- **Geração de Quizzes** com perguntas baseadas nas palavras/expressões dos textos.

## Tecnologias Utilizadas

- **FastAPI**: Framework rápido e moderno para APIs em Python.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **OpenAI**: Utilizado para gerar flashcards e quizzes com base nos textos enviados pelos usuários.
- **JWT**: Para autenticação de usuários.
- **SQLite**: Banco de dados utilizado para armazenar informações de usuários e atividades.
- **Vue.js**: Framework para o desenvolvimento do front-end.
- **Vite**: Build tool para otimizar a construção do projeto Vue.js.

## Rodando o Backend

### Requisitos

- Python 3.8 ou superior.
- Pip (gerenciador de pacotes do Python).

### Passo 1: Instalar dependências

Clone o repositório e instale as dependências do projeto utilizando o `pip`:

```bash
git clone <url-do-repositorio>
cd nome-do-repositorio
pip install -r backend/requirements.txt
````

### Passo 2: Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto e adicione a chave da API do OpenAI. Exemplo:

```env
OPENAI_API_KEY=sua-chave-api-aqui
```

### Passo 3: Iniciar o banco de dados

O banco de dados será criado automaticamente quando você rodar o backend pela primeira vez. No entanto, você pode executar a criação das tabelas manualmente com:

```bash
python
from backend.main import Base, engine
Base.metadata.create_all(bind=engine)
```

### Passo 4: Rodar o servidor

Para rodar o backend, execute o comando:

```bash
uvicorn backend.main:app --reload
```

Isso iniciará o servidor FastAPI na URL `http://127.0.0.1:8000`. Você pode acessar a documentação interativa da API em `http://127.0.0.1:8000/docs`.

## Rodando o Frontend

### Requisitos

* Node.js (versão recomendada: 16.x ou superior)
* npm ou yarn

### Passo 1: Instalar dependências

No diretório do projeto, vá para a pasta do **frontend** e instale as dependências com npm ou yarn:

```bash
cd frontend
npm install
# ou, se usar yarn
yarn install
```

### Passo 2: Rodar o servidor de desenvolvimento

Para rodar o frontend, execute o comando:

```bash
npm run dev
# ou, se usar yarn
yarn dev
```

Isso iniciará o servidor de desenvolvimento na URL `http://localhost:5173`. Você pode acessar a interface do usuário do seu sistema de aprendizado de inglês.

## Estrutura do Frontend

A estrutura do frontend é construída com **Vue.js** e **Vite**.

* **App.vue**: Componente principal do aplicativo, que serve como ponto de entrada para os outros componentes.
* **main.js**: Configuração inicial para o Vue.js e o roteamento com Vue Router.
* **Vite**: Ferramenta usada para otimizar o processo de desenvolvimento e build. A configuração está no arquivo `vite.config.js`.

## Endpoints Backend

### 1. **POST /register**

Cria um novo usuário.

#### Corpo da requisição:

```json
{
  "email": "usuario@exemplo.com",
  "senha": "senha_secreta"
}
```

### 2. **POST /login**

Faz login e retorna um token de autenticação.

#### Corpo da requisição:

```json
{
  "email": "usuario@exemplo.com",
  "senha": "senha_secreta"
}
```

### 3. **POST /atividades**

Cria uma nova atividade de aprendizado, gerando flashcards e quiz a partir do texto enviado.

#### Corpo da requisição:

```json
{
  "nome": "Atividade 1",
  "prompt": "Texto do usuário para gerar flashcards e quiz",
  "flashcards": "Flashcards gerados pela IA",
  "quiz": "Quiz gerado pela IA"
}
```

### 4. **GET /atividades**

Retorna as atividades de aprendizado do usuário autenticado.

### 5. **POST /gerar-flashcards**

Gera flashcards a partir de um texto enviado.

#### Corpo da requisição:

```json
{
  "texto": "Texto do usuário"
}
```

### 6. **POST /gerar-quiz**

Gera um quiz a partir de um texto enviado.

#### Corpo da requisição:

```json
{
  "texto": "Texto do usuário"
}
```

## Contribuindo

Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`).
3. Faça commit das suas alterações (`git commit -am 'Adicionando minha feature'`).
4. Push para a branch (`git push origin feature/MinhaFeature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

```
