"""
Repositorio de clientes para MongoDB.

Este módulo proporciona las operaciones CRUD básicas para la colección 'clientes' 
de la base de datos 'btg_fondos'.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
"""

from app.adapters.mongo.database import get_database
from bson import ObjectId

class RepoClientesMongo:
    """
    Repositorio para interactuar con la colección 'clientes'.

    Métodos:
        listar_clientes(): Devuelve la lista de todos los clientes.
        obtener_cliente_por_id(cliente_id): Obtiene un cliente por su ID.
    """

    def __init__(self):
        """
        Inicializa el repositorio conectándose a la colección 'clientes' de MongoDB.

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        db = get_database()
        self.collection = db["clientes"]

    def listar_clientes(self):
        """
        Lista todos los clientes almacenados en la colección.

        Returns:
            List[dict]: Lista de clientes con campos:
                        id, nombres, apellidos, correo_electronico,
                        telefono, celular, direccion, saldo

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        clientes = []
        for doc in self.collection.find():
            clientes.append({
                "id": str(doc.get("_id")),
                "nombres": doc.get("nombres"),
                "apellidos": doc.get("apellidos"),
                "correo_electronico": doc.get("correo_electronico"),
                "telefono": doc.get("telefono"),
                "celular": doc.get("celular"),
                "direccion": doc.get("direccion"),
                "saldo": doc.get("saldo")
            })
        return clientes

    def obtener_cliente_por_id(self, cliente_id: int):
        """
        Obtiene un cliente específico por su ID.

        Args:
            cliente_id (int): ID del cliente a buscar.

        Returns:
            dict | None: Diccionario con los datos del cliente si se encuentra,
                         None en caso contrario.

        Author: Aura Cristina Garzón Rodríguez
        Version: 1.0
        Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
        """
        doc = self.collection.find_one({"_id": cliente_id})
        if doc:
            return {
                "id": doc.get("_id"),
                "nombres": doc.get("nombres"),
                "apellidos": doc.get("apellidos"),
                "correo_electronico": doc.get("correo_electronico"),
                "telefono": doc.get("telefono"),
                "celular": doc.get("celular"),
                "direccion": doc.get("direccion"),
                "saldo": doc.get("saldo")
            }
        return None
