"""
Servicio de dominio para la gestión de fondos.

el servicio no debería crear directamente su repositorio interno, sino recibirlo por parámetro. Esto respeta los principios:

DIP (Dependency Inversion Principle): la clase depende de una abstracción (un repositorio) en lugar de una implementación concreta.

SRP (Single Responsibility Principle): la clase solo gestiona la lógica de negocio de fondos, no decide cómo obtenerlos.

Facilita tests unitarios: podemos pasar un mock de repositorio sin tocar MongoDB.

Este servicio expone operaciones relacionadas con los fondos, como
listar todos los fondos disponibles. Se encarga de aplicar la
lógica de negocio y delega la persistencia a los repositorios.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: Bogotá D.C., Colombia
"""

from app.adapters.mongo.repo_fondos import RepoFondosMongo
from app.ports.repository import IRepoFondos  # idealmente usar interfaz

class FondosService:
    def __init__(self, repo: IRepoFondos):
        """
        Inicializa el servicio de fondos.

        Args:
            repo: Instancia de un repositorio que cumpla la interfaz IRepoFondos.
        """
        self.repo = repo

    def listar_fondos(self):
        """
        Retorna la lista de todos los fondos disponibles.
        """
        return self.repo.listar_fondos()
    
    def crear_fondo(self, nombre: str, monto_minimo: float, categoria: str) -> dict:
        """
        Crea un nuevo fondo con validaciones de negocio.

        Args:
            nombre (str): Nombre del fondo.
            monto_minimo (float): Monto mínimo requerido.
            categoria (str): Categoría del fondo.

        Returns:
            dict: Fondo creado con su ID asignado.
        """
        if monto_minimo <= 500000:
            raise ValueError("El monto mínimo debe ser mayor a 500000")

        fondo = {
            "nombre": nombre,
            "monto_minimo": monto_minimo,
            "categoria": categoria
        }

        fondo_id = self.repo.crear_fondo(fondo)

        return {**fondo, "id": fondo_id}    
    
    