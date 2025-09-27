"""
Esquemas Pydantic para la API de suscripciones de fondos.

Define los modelos de entrada y salida que se utilizan en los endpoints
de suscripción, garantizando la validación de los datos y la estructura
de la respuesta.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27, Bogotá D.C., Colombia
"""

from pydantic import BaseModel


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
