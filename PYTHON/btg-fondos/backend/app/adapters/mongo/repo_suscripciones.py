"""
Repositorio de suscripciones para MongoDB.

Este módulo proporciona las operaciones CRUD básicas para la colección 'suscripciones' 
de la base de datos 'btg_fondos'.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
"""

from app.adapters.mongo.database import get_database
from app.domain.entities import Suscripcion

import datetime
from bson import ObjectId

class RepoSuscripcionesMongo:
    """
    Repositorio para interactuar con la colección 'suscripciones'.

    Métodos:
        crear(cliente_id, fondo_id, monto): Crea una nueva suscripción.
        listar(): Devuelve todas las suscripciones existentes.
    """

    def __init__(self):
        """
        Inicializa el repositorio conectándose a la colección 'suscripciones' de MongoDB.

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        db = get_database()
        self.collection = db["suscripciones"]

    def crear(self, suscripcion: Suscripcion):
        """
        Crea una nueva suscripción para un cliente en un fondo específico.

        Args:
            cliente_id (str): ID del cliente.
            fondo_id (str): ID del fondo.
            monto (float): Monto de la inversión inicial.

        Returns:
            dict: Documento de la suscripción creada, incluyendo:
                  id, cliente_id, fondo_id, monto, tipo, fecha

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        doc = {
            "cliente_id": suscripcion.cliente_id,
            "fondo_id": suscripcion.fondo_id,
            "monto": suscripcion.monto,
            "tipo": "apertura",
            "fecha": datetime.datetime.now().isoformat()
        }
        result = self.collection.insert_one(doc)
        doc["_id"] = str(result.inserted_id)
        return doc

    def listar(self):
        """
        Lista todas las suscripciones almacenadas en la colección.

        Returns:
            List[dict]: Lista de suscripciones con campos:
                        id, cliente_id, fondo_id, monto, tipo, fecha

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        suscripciones = []
        for doc in self.collection.find():
            suscripciones.append({
                "id": str(doc.get("_id")),
                "cliente_id": str(doc.get("cliente_id")),
                "fondo_id": str(doc.get("fondo_id")),
                "monto": doc.get("monto"),
                "tipo": doc.get("tipo"),
                "fecha": doc.get("fecha")
            })
        return suscripciones
