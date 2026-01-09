from fastapi import FastAPI
from contextlib import asynccontextmanager
from rotas import home, users, posts, tags
from database import init_db, close_db
from fastapi_pagination import add_pagination

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()

# FastAPI app instance
app = FastAPI(lifespan=lifespan)

# Rotas para Endpoints
app.include_router(home.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(tags.router)
add_pagination(app)