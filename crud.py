from sqlalchemy.orm import Session
import database, models, schemas

def create_client(db: Session, client: schemas.ClientCreate):
    data = client.model_dump(exclude_unset=True)
    db_client = models.Client(**data)
    
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    
    return db_client