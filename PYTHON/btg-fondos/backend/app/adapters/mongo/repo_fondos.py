"""
Repositorio de fondos para MongoDB.

Este módulo proporciona las operaciones CRUD básicas para la colección 'fondos' 
de la base de datos 'btg_fondos'.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
"""

from app.adapters.mongo.database import get_database
from typing import Dict, List


class RepoFondosMongo:
    """
    Repositorio para interactuar con la colección 'fondos'.

    Métodos:
        listar_fondos(): Devuelve la lista de todos los fondos.
    """

    def __init__(self):
        """
        Inicializa el repositorio conectándose a la colección 'fondos' de MongoDB.

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        db = get_database()
        self.collection = db["fondos"]

    def listar_fondos(self):
        """
        Lista todos los fondos almacenados en la colección.

        Returns:
            List[dict]: Lista de fondos con campos:
                        id, nombre, categoria, monto_minimo

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        fondos = []
        for doc in self.collection.find():
            fondos.append({
                "id": doc.get("_id"),
                "nombre": doc.get("nombre"),
                "categoria": doc.get("categoria"),
                "monto_minimo": doc.get("monto_minimo")
            })
        return fondos
    
    def crear_fondo(self, fondo: Dict) -> int:
        """
        Crea un fondo con un ID numérico consecutivo.
        
        Args:
            fondo (Dict): Datos del fondo.
        Returns:
            int: ID numérico asignado al fondo.
        """
        # Buscar el máximo ID actual
        ultimo_fondo = self.collection.find_one(sort=[("_id", -1)])
        nuevo_id = (ultimo_fondo["_id"] + 1) if ultimo_fondo and "_id" in ultimo_fondo else 1

        # Asignar el nuevo ID al documento
        fondo["_id"] = nuevo_id

        # Insertar el fondo en la colección
        self.collection.insert_one(fondo)

        return nuevo_id