from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import logging
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configurar o logger
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Configuração do banco de dados
engine = create_engine(os.getenv("DATABASE_URL"))
