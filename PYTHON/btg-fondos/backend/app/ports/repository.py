from abc import ABC, abstractmethod
from typing import List
from app.domain.entities import Cliente, Fondo, Suscripcion

class IRepoClientes(ABC):
    @abstractmethod
    def get_by_id(self, cliente_id: str) -> Cliente: ...
    @abstractmethod
    def save(self, cliente: Cliente) -> None: ...

class IRepoFondos(ABC):
    @abstractmethod
    def listar(self) -> List[Fondo]: ...

class IRepoSuscripciones(ABC):
    @abstractmethod
    def crear(self, suscripcion: Suscripcion) -> None: ...
