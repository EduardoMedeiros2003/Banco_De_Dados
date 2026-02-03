from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

# Cria as tabelas no PostgreSQL (caso nào existam) 
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.clsse()

# Salvando no Banco de Dados
@app.post('/estudante/', response_model=schemas.EstudanteResponse)
def create_student(student: schemas.EstudanteCreate, db: Session = Depends(get_bd)):
    db_estudante = models.Estudantes(**student.model_dump())# Dicionarios .jason|Metodo de adicionar um estudante diretamente do navegador
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante
    
@app.get('/estudante', response_model=List[schemas.EstudanteResponse])
def read_students(db: Session = Depends(get_bd())):
    students = db.query(models.Estudantes).all()# Fusque todas as ocorrencias do banco de dados
    return students