from app.adapters.mongo.client import get_database

class RepoFondosMongo:
    def __init__(self):
        db = get_database()
        self.collection = db["fondos"]

    def listar_fondos(self):
        fondos = []
        for doc in self.collection.find():
            fondos.append({
                "id": str(doc.get("_id")),
                "nombre": doc.get("nombre"),
                "categoria": doc.get("categoria"),
                "valor_unitario": doc.get("valor_unitario")
            })
        return fondos
