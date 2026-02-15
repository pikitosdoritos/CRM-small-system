from fastapi import FastAPI, HTTPException
from .database import Base, engine

app = FastAPI()

@app.on_event("startup")
def startup_seed():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}