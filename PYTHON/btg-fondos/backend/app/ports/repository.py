"""
Puertos (Interfaces) de la capa de dominio.

Aquí se definen las abstracciones que permiten desacoplar
el núcleo de negocio de las implementaciones concretas de persistencia.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27, Bogotá D.C., Colombia
"""

from abc import ABC, abstractmethod
from typing import List, Dict
from app.domain.entities import Cliente, Fondo, Suscripcion


class IRepoClientes(ABC):
    """
    Interfaz para el repositorio de clientes.

    Define los métodos que cualquier implementación concreta de acceso a clientes
    debe proporcionar, permitiendo la abstracción de la capa de persistencia.
    """

    @abstractmethod
    def get_by_id(self, cliente_id: str) -> Cliente:
        """Obtiene un cliente por su identificador único."""
        ...

    @abstractmethod
    def save(self, cliente: Cliente) -> None:
        """Guarda un cliente en el repositorio."""
        ...


class IRepoFondos(ABC):
    """
    Interfaz para el repositorio de fondos.

    Define los métodos que cualquier implementación concreta de acceso a fondos
    debe proporcionar.
    """

    @abstractmethod
    def listar(self) -> List[Fondo]:
        """
        Lista todos los fondos disponibles.

        Returns:
            List[Fondo]: Lista de objetos Fondo.
        """
        ...

    @abstractmethod
    def crear_fondo(self, fondo: Dict) -> str:
        """
        Crea un nuevo fondo en la base de datos.

        Args:
            fondo (Dict): Datos del fondo a crear.
        Returns:
            str: ID del fondo creado.
        """
        ...


class IRepoSuscripciones(ABC):
    """
    Interfaz para el repositorio de suscripciones.

    Define los métodos que cualquier implementación concreta de gestión de
    suscripciones debe proporcionar.
    """

    @abstractmethod
    def crear(self, suscripcion: Suscripcion) -> None:
        """
        Crea una nueva suscripción.

        Args:
            suscripcion (Suscripcion): Objeto Suscripcion a registrar.
        """
        ...
