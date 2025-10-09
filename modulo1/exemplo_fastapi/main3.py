import logging
from fastapi import FastAPI, Body

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s")

# Cria um logger para esta aplicação
logger = logging.getLogger("fastapi.app")

app = FastAPI()

@app.get("/")
def home():
    logger.info("Rota '/' acessada.")
    return {"msg": "Olá, mundo!"}

@app.get("/posts/{id}")
def get_post(id: int, titulo: str | None = None):
    logger.info(f"GET /posts/{id} chamado com titulo={titulo!r}")
    return {"id": id, "titulo": titulo}

@app.post("/posts/{id}/titulo")
def read_post_str(id: int, titulo: str = Body(default=None)):
    return {"id": id, "titulo": titulo}

@app.post("/posts/{id}")
def read_post_json(id: int, body: dict = Body(default=None)):
    return {"id": id, "titulo": body.get("titulo")}