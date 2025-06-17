from pydantic import BaseModel


# ---------- USUÁRIO ----------


class UserCreate(BaseModel):
    email: str
    senha: str


class UserLogin(BaseModel):
    email: str
    senha: str


# ---------- ATIVIDADE ----------


class AtividadeBase(BaseModel):
    nome: str
    prompt: str
    flashcards: str
    quiz: str


class AtividadeOut(AtividadeBase):
    id: int

    class Config:
        orm_mode = True
