from datetime import datetime
from pydantic import BaseModel

class Cliente(BaseModel):
    id: str
    nombre: str
    correo: str

class Fondo(BaseModel):
    id: str
    nombre: str
    categoria: str

class Suscripcion(BaseModel):
    cliente_id: str
    fondo_id: str
    fecha: datetime = datetime.utcnow()
