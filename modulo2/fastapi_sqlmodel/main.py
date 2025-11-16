from fastapi import FastAPI, Depends
from sqlmodel import select, Session
from database import get_session
from models import Aluno

app = FastAPI()

@app.get("/")
def home():
	return {"msg": "Funcionando!!!"}

@app.post("/alunos", response_model=Aluno)
def inserir_aluno(aluno: Aluno, session: Session = Depends(get_session)) -> Aluno:
	session.add(aluno)
	session.commit()
	session.refresh(aluno)
	return aluno

@app.get("/alunos", response_model=list[Aluno])
def listar_alunos(session: Session = Depends(get_session)) -> list[Aluno]:
	alunos = session.exec(select(Aluno)).all()
	return alunos
