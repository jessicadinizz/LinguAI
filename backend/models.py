from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)

    atividades = relationship("Atividade", back_populates="criador")


class Atividade(Base):
    __tablename__ = "atividades"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    prompt = Column(Text, nullable=False)
    flashcards = Column(Text, nullable=False)
    quiz = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    criador = relationship("User", back_populates="atividades")
