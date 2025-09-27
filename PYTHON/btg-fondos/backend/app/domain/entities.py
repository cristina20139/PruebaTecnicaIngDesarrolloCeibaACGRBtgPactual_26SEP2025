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

class Suscripcion:
    def __init__(self, cliente_id: str, fondo_id: str, monto: float):
        self.cliente_id = cliente_id
        self.fondo_id = fondo_id
        self.monto = monto
        self.tipo = "apertura"
        self.fecha = datetime.now().isoformat()
