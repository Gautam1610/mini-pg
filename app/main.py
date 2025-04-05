from fastapi import FastAPI
from app.db.session import engine
from app.models.base import Base

Base.metadata.create_all(bind=engine)


app = FastAPI()