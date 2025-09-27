"""
Servicio de dominio para la gestión de fondos.

Este servicio expone operaciones relacionadas con los fondos, como
listar todos los fondos disponibles. Se encarga de aplicar la
lógica de negocio y delega la persistencia a los repositorios.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: Bogotá D.C., Colombia
"""

from app.adapters.mongo.repo_fondos import RepoFondosMongo

class FondosService:
    def __init__(self, repo=None):
        """
        Inicializa el servicio de fondos.

        Args:
            repo (optional): Instancia del repositorio de fondos. Si no se
                             proporciona, se crea una instancia de RepoFondosMongo.
        """
        self.repo = repo or RepoFondosMongo()

    def listar_fondos(self):
        """
        Retorna la lista de todos los fondos disponibles.

        Returns:
            list: Lista de fondos con sus atributos principales, incluyendo
                  id, nombre, categoría y monto mínimo.
        """
        return self.repo.listar_fondos()
