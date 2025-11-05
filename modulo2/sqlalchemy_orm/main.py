from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Aluno
from database import engine
import settings

engine = create_engine(settings.DATABASE_URL)

# Criar a(s) tabela(s) no banco de dados
Base.metadata.create_all(engine)

with Session(engine) as session:
	# Inserir novos registros
	try:
		session.add(Aluno(nome='Maria', apelido='Mari'))
		session.add(Aluno(nome='João'))
		session.commit()
	except Exception as e:
		session.rollback()
		print(f'Erro: {e}')

	# Consultar registros
	alunos = session.query(Aluno).all()
	for aluno in alunos:
		print(aluno)