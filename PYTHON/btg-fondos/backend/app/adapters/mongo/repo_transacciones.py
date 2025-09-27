"""
Repositorio de transacciones para MongoDB.

Este módulo proporciona las operaciones CRUD básicas para la colección 'transacciones' 
de la base de datos 'btg_fondos'.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
"""

from app.adapters.mongo.database import get_database
from app.domain.entities import Transaccion

class RepoTransaccionesMongo:
    """
    Repositorio para interactuar con la colección 'transacciones'.

    Métodos:
        crear(transaccion: Transaccion): Guarda una nueva transacción.
        listar_por_cliente(cliente_id: int): Lista todas las transacciones de un cliente.
    """

    def __init__(self):
        """
        Inicializa el repositorio conectándose a la colección 'transacciones' de MongoDB.

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        db = get_database()
        self.collection = db["transacciones"]

    def crear(self, transaccion: Transaccion):
        """
        Guarda una nueva transacción en la colección.

        Args:
            transaccion (Transaccion): Objeto de dominio Transaccion.

        Returns:
            InsertOneResult: Resultado de la inserción en MongoDB.
        """
        doc = {
            "cliente_id": transaccion.cliente_id,
            "fondo_id": transaccion.fondo_id,
            "tipo": transaccion.tipo,
            "monto": transaccion.monto,
            "fecha": transaccion.fecha
        }
        return self.collection.insert_one(doc)

    def listar_por_cliente(self, cliente_id: int):
        """
        Lista todas las transacciones de un cliente por su ID.

        Args:
            cliente_id (int): ID del cliente.

        Returns:
            List[Transaccion]: Lista de objetos Transaccion.
        """
        docs = self.collection.find({"cliente_id": cliente_id})
        return [Transaccion(
            cliente_id=doc["cliente_id"],
            fondo_id=doc["fondo_id"],
            tipo=doc["tipo"],
            monto=doc["monto"]
        ) for doc in docs]
