"""
Modelos de dominio para Clientes, Fondos y Suscripciones.

Este módulo define las clases que representan las entidades principales 
del sistema de gestión de fondos.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
"""

from datetime import datetime
from pydantic import BaseModel

class Cliente(BaseModel):
    """
    Representa un cliente del sistema.

    Attributes:
        id (str): Identificador único del cliente.
        nombre (str): Nombre completo del cliente.
        correo (str): Correo electrónico del cliente.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
    """
    id: int
    nombre: str
    correo: str

class Fondo(BaseModel):
    """
    Representa un fondo de inversión.

    Attributes:
        id (str): Identificador único del fondo.
        nombre (str): Nombre del fondo.
        categoria (str): Categoría del fondo.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
    """
    id: int
    nombre: str
    categoria: str

class Suscripcion:
    """
    Representa la suscripción de un cliente a un fondo.

    Attributes:
        cliente_id (str): ID del cliente que realiza la suscripción.
        fondo_id (str): ID del fondo al que se suscribe el cliente.
        monto (float): Monto invertido en la suscripción.
        tipo (str): Tipo de operación, por defecto 'apertura'.
        fecha (str): Fecha y hora de la suscripción en formato ISO.

    Methods:
        __init__(cliente_id, fondo_id, monto): Inicializa una nueva suscripción.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
    """

    def __init__(self, cliente_id: str, fondo_id: str, monto: float):
        """
        Inicializa una nueva suscripción para un cliente a un fondo.

        Args:
            cliente_id (str): ID del cliente.
            fondo_id (str): ID del fondo.
            monto (float): Monto de inversión inicial.

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        self.cliente_id = cliente_id
        self.fondo_id = fondo_id
        self.monto = monto
        self.tipo = "apertura"
        self.fecha = datetime.now().isoformat()
