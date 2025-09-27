from pydantic import BaseModel

class SuscripcionRequest(BaseModel):
    cliente_id: int
    monto: float

class SuscripcionResponse(BaseModel):
    cliente_id: str
    fondo_id: str
    monto: float
    tipo: str
    fecha: str
