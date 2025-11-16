from sqlmodel import Session, select
from models import Aluno
from database import engine

with Session(engine) as session:
	try:
		session.add(Aluno(nome='Maria', apelido='Mari'))
		session.add(Aluno(nome='João'))
		session.commit()
	except Exception as e:
		session.rollback()
		print(f'Erro: {e}')

	alunos = session.exec(select(Aluno)).all()
	for aluno in alunos:
		print(aluno)