from datetime import datetime
from app.domain.errors import ClienteNoEncontrado, FondoNoEncontrado

class Suscripcion:
    def __init__(self, cliente_id: str, fondo_id: str, monto: float):
        self.cliente_id = cliente_id
        self.fondo_id = fondo_id
        self.monto = monto
        self.tipo = "apertura"
        self.fecha = datetime.now().isoformat()

class SubscriptionService:
    def __init__(self, repo_clientes, repo_fondos, repo_suscripciones):
        self.repo_clientes = repo_clientes
        self.repo_fondos = repo_fondos
        self.repo_suscripciones = repo_suscripciones

    def suscribir(self, cliente_id: str, fondo_id: str, monto: float):
        cliente = self.repo_clientes.obtener_cliente_por_id(cliente_id)
        if not cliente:
            raise ClienteNoEncontrado(f"Cliente {cliente_id} no encontrado")

        fondos = self.repo_fondos.listar_fondos()
        if not any(f["id"] == fondo_id for f in fondos):
            raise FondoNoEncontrado(f"Fondo {fondo_id} no encontrado")

        suscripcion = Suscripcion(cliente_id=cliente_id, fondo_id=fondo_id, monto=monto)
        self.repo_suscripciones.crear(suscripcion)
        return suscripcion
