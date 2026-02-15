from fastapi import FastAPI, HTTPException, Depends
from .database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import crud, schemas, models

app = FastAPI(title="CRM API", version="0.0.1")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_seed():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/clients", tags=["clients"])
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_client(db=db, client=client)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Client already exists")