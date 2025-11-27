from fastapi import FastAPI
from sqlmodel import Session, select
from app.models.item import Item
from app.core.config import settings

from app.api.api import api_router

app = FastAPI(title="JMTech E-commerce API", version="0.1.0")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to JMTech E-commerce API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
