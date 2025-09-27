"""
Esquemas Pydantic para la API de suscripciones de fondos.

Define los modelos de entrada y salida que se utilizan en los endpoints
de suscripción, garantizando la validación de los datos y la estructura
de la respuesta.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27, Bogotá D.C., Colombia
"""

from pydantic import BaseModel, Field
from typing import Optional


class SuscripcionRequest(BaseModel):
    """
    Modelo de solicitud para suscribirse a un fondo.

    Attributes:
        cliente_id (int): ID del cliente que realiza la suscripción.
        monto (float): Monto de inversión para la suscripción.
    """
    cliente_id: int
    monto: float


class SuscripcionResponse(BaseModel):
    """
    Modelo de respuesta tras crear una suscripción.

    Attributes:
        cliente_id (str): ID del cliente suscrito.
        fondo_id (str): ID del fondo al que se suscribió.
        monto (float): Monto invertido en la suscripción.
        tipo (str): Tipo de transacción (por ejemplo, "apertura").
        fecha (str): Fecha y hora de creación de la suscripción en formato ISO.
    """
    cliente_id: int
    fondo_id: int
    monto: float
    tipo: str
    fecha: str

class FondoRequest(BaseModel):
    nombre: str = Field(..., example="Fondo de Inversión ACGR")
    monto_minimo: float = Field(..., gt=0, example=1000.0)
    categoria: str = Field(..., example="Renta fija")

class FondoResponse(BaseModel):
    id: int
    nombre: str
    monto_minimo: float
    categoria: str

class ClienteUpdate(BaseModel):
    nombres: Optional[str] = Field(None, example="Aura Cristina")
    apellidos: Optional[str] = Field(None, example="Garzón Rodríguez")
    correo_electronico: Optional[str] = Field(None, example="acgarzon@example.com")
    telefono: Optional[str] = Field(None, example="6011234567")
    celular: Optional[str] = Field(None, example="3001234567")
    direccion: Optional[str] = Field(None, example="Calle 123 #45-67, Bogotá")
    saldo: Optional[float] = Field(None, example=1500000.0)