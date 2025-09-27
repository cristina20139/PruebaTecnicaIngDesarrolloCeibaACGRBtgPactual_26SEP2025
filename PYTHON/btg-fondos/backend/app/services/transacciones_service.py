from app.adapters.mongo.repo_transacciones import RepoTransaccionesMongo
from app.domain.entities import Transaccion

class TransaccionesService:
    """
    Servicio de transacciones.

    Coordina la lógica de negocio para manejar las transacciones de los clientes.
    """

    def __init__(self, repo_transacciones: RepoTransaccionesMongo):
        self.repo_transacciones = repo_transacciones

    def listar_transacciones_por_cliente(self, cliente_id: int):
        """
        Lista todas las transacciones de un cliente.

        Args:
            cliente_id (int): ID del cliente.

        Returns:
            List[dict]: Lista de transacciones en formato diccionario.
        """
        transacciones = self.repo_transacciones.listar_por_cliente(cliente_id)
        # Convertimos los objetos Transaccion a diccionarios
        return [
            {
                "cliente_id": t.cliente_id,
                "fondo_id": t.fondo_id,
                "tipo": t.tipo,
                "monto": t.monto,
                "fecha": t.fecha
            }
            for t in transacciones
        ]
