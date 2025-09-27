# app/adapters/mongo/repo_clientes.py
from app.adapters.mongo.database import get_database

class RepoClientesMongo:
    def __init__(self):
        db = get_database()
        self.collection = db["clientes"]  # colección clientes

    def listar_clientes(self):
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

    def obtener_cliente_por_id(self, cliente_id):
        doc = self.collection.find_one({"_id": cliente_id})
        if doc:
            return {
                "id": str(doc.get("_id")),
                "nombres": doc.get("nombres"),
                "apellidos": doc.get("apellidos"),
                "correo_electronico": doc.get("correo_electronico"),
                "telefono": doc.get("telefono"),
                "celular": doc.get("celular"),
                "direccion": doc.get("direccion"),
                "saldo": doc.get("saldo")
            }
        return None
