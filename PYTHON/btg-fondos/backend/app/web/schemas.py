from pydantic import BaseModel

class SuscripcionRequest(BaseModel):
    cliente_id: str
    fondo_id: str

class SuscripcionResponse(BaseModel):
    cliente_id: str
    fondo_id: str
