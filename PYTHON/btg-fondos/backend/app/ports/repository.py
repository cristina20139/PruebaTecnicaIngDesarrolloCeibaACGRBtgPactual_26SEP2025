from abc import ABC, abstractmethod
from typing import List
from app.domain.entities import Cliente, Fondo, Suscripcion

class IRepoClientes(ABC):
    """
    Interfaz para el repositorio de clientes.

    Define los métodos que cualquier implementación concreta de acceso a clientes
    debe proporcionar, permitiendo la abstracción de la capa de persistencia.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27, Bogotá D.C., Colombia
    """

    @abstractmethod
    def get_by_id(self, cliente_id: str) -> Cliente:
        """
        Obtiene un cliente por su identificador.

        Args:
            cliente_id (str): Identificador único del cliente.

        Returns:
            Cliente: Objeto Cliente correspondiente al ID proporcionado.

        Raises:
            DomainError: Si no se encuentra el cliente.
        """
        ...

    @abstractmethod
    def save(self, cliente: Cliente) -> None:
        """
        Guarda un cliente en el repositorio.

        Args:
            cliente (Cliente): Objeto Cliente a persistir.
        """
        ...


class IRepoFondos(ABC):
    """
    Interfaz para el repositorio de fondos.

    Define los métodos que cualquier implementación concreta de acceso a fondos
    debe proporcionar.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27, Bogotá D.C., Colombia
    """

    @abstractmethod
    def listar(self) -> List[Fondo]:
        """
        Lista todos los fondos disponibles.

        Returns:
            List[Fondo]: Lista de objetos Fondo.
        """
        ...


class IRepoSuscripciones(ABC):
    """
    Interfaz para el repositorio de suscripciones.

    Define los métodos que cualquier implementación concreta de gestión de
    suscripciones debe proporcionar.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27, Bogotá D.C., Colombia
    """

    @abstractmethod
    def crear(self, suscripcion: Suscripcion) -> None:
        """
        Crea una nueva suscripción.

        Args:
            suscripcion (Suscripcion): Objeto Suscripcion a registrar.
        """
        ...
