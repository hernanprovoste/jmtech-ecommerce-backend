from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from app.models.item import Item
from app.core.config import settings

from app.api.api import api_router

app = FastAPI(title="JMTech E-commerce API", version="0.1.0")

origins = [
    "http://localhost:3000", # Frontend local
    "https://tu-dominio-vercel.app", # Domain Vercel
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to JMTech E-commerce API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
