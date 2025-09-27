from app.adapters.mongo.repo_suscripciones import RepoSuscripcionesMongo
from app.adapters.mongo.repo_clientes import RepoClientesMongo

class SaldoService:
    """
    Servicio para consultar el saldo disponible de un cliente.
    """

    def __init__(self, repo_clientes: RepoClientesMongo, repo_suscripciones: RepoSuscripcionesMongo):
        self.repo_clientes = repo_clientes
        self.repo_suscripciones = repo_suscripciones

    def obtener_saldo(self, cliente_id: int) -> float:
        """
        Calcula el saldo disponible de un cliente.

        Args:
            cliente_id (int): ID del cliente.

        Returns:
            float: Saldo disponible para nuevas suscripciones.
        """
        cliente = self.repo_clientes.obtener_cliente_por_id(cliente_id)
        if not cliente:
            raise ValueError(f"Cliente {cliente_id} no encontrado")

        # Obtenemos todas las suscripciones del cliente
        suscripciones = self.repo_suscripciones.listar_por_cliente(cliente_id)

        # Calculamos el total invertido
        total_invertido = sum(s.monto for s in suscripciones)

        # Supongamos que cada cliente tiene un saldo inicial de 100000 (esto se puede ajustar)
        saldo_inicial = 0

        saldo_disponible = saldo_inicial - total_invertido
        return max(saldo_disponible, 0)  # Nunca negativo
