from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
	nome: str
	valor: float
	is_oferta: bool | None = None

@app.get("/")
def read_root():
	return {"msg": "Hello World"}

@app.get("/itens/{id}")
def le_id_item(id: int):
	return id

@app.post("/itens/")
def le_item(item: Item):
	return item