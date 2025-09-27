from app.adapters.mongo.repo_clientes import RepoClientesMongo

class ClientesService:
    """
    Servicio de clientes.

    Esta clase actúa como capa de servicio para operaciones relacionadas con
    clientes, delegando la persistencia al repositorio RepoClientesMongo.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27, Bogotá D.C., Colombia
    """

    def __init__(self, repo_clientes):
        self.repo_clientes = repo_clientes

    def listar_clientes(self):
        """
        Obtiene la lista de todos los clientes.

        Returns:
            list: Lista de diccionarios con la información de cada cliente.
        """
        return self.repo_clientes.listar_clientes()

    def obtener_cliente(self, cliente_id):
        """
        Obtiene la información de un cliente por su identificador.

        Args:
            cliente_id: Identificador único del cliente.

        Returns:
            dict | None: Diccionario con la información del cliente si existe,
            de lo contrario None.
        """
        return self.repo_clientes.obtener_cliente_por_id(cliente_id)
