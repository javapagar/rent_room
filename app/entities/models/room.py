import uuid
from pydantic import BaseModel

class Room(BaseModel):
    uuid: uuid.UUID
    price: int
    size: int
    lon: float
    lat: float