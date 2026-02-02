from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

DATABASE_URL = "postagresql://postgres:postgres@localhost/escola" #URL do Banco de Dados

engine = create_engine(DATABASE_URL)#Motor do Banco de dados
SessionLocal = sessionmaker(bind=engine)#Faz a conexão do sistema com o banco

Base = declarative_base()# Modelo do Banco de Dados
