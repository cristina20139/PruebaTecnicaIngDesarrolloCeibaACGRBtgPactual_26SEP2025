from typing import Optional
from app.domain.entities import Cliente
from app.ports.repository import IRepoClientes
from .client import get_mongo_client

class MongoRepoClientes(IRepoClientes):
    def __init__(self, db_name: str = "btg_fondos"):
        client = get_mongo_client()
        self.collection = client[db_name]["clientes"]

    def save(self, cliente: Cliente) -> str:
        result = self.collection.insert_one(cliente.dict())
        return str(result.inserted_id)

    def find_by_email(self, email: str) -> Optional[Cliente]:
        doc = self.collection.find_one({"correo_electronico": email})
        if doc:
            return Cliente(**doc)
        return None

    def list_all(self) -> list[Cliente]:
        docs = self.collection.find()
        return [Cliente(**doc) for doc in docs]
