from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title=settings.project_name,
    version=settings.project_version,
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {"project": settings.project_name}


@app.get("/health")
async def health():
    return {"status": "ok"}
