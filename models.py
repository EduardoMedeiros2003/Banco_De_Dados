from sqlalchemy import Column,Integer, String, ForeignKey
from database import Base

class Estudantes(Base):
    __tablename__ = 'estudante'
    id = Column(Integer, primary_key=True, index=True)# id_estudante, coluna - inteiro - chave primaria - vai cirar altomaticamente(index)
    nome = Column(String(100), nullable=False)#nome, coluna - string - nao pode esta vazio
    idade = Column(Integer)

class Matricula(Base):
    __tablename__ = 'matricula'
    id = Column(Integer, primary_key=True, index=True)#id_matricula, coluna , chave primaria- vai criar altomaticamente
    estudante_id = Column(Integer, ForeignKey('estudante.id'))#id_estudante, coluna - inteiro - chave estrangeira
    nome_disciplina = Column(String(100), nullable=False)