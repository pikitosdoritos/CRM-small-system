from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ClientCreate(BaseModel):
    name: str
    email: str
    phone_number: Optional[str]
    status: str 
        
class ClientResponse(BaseModel):
    id: int
    name: str
    email: str
    phone_number: Optional[str] 
    status: str 
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)