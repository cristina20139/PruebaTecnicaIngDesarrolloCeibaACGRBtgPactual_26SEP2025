# app/adapters/mongo/repo_suscripciones.py
from app.adapters.mongo.database import get_database
import datetime
from bson import ObjectId

class RepoSuscripcionesMongo:
    def __init__(self):
        db = get_database()
        self.collection = db["suscripciones"]  # colección suscripciones

    def crear(self, cliente_id: str, fondo_id: str, monto: float):
        doc = {
            "cliente_id": str(cliente_id),
            "fondo_id": str(fondo_id),
            "monto": monto,
            "tipo": "apertura",
            "fecha": datetime.datetime.now().isoformat()
        }
        result = self.collection.insert_one(doc)
        doc["_id"] = str(result.inserted_id)
        return doc

    def listar(self):
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
