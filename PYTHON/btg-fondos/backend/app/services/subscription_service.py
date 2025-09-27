from app.domain.entities import Suscripcion
from app.ports.repository import IRepoClientes, IRepoFondos, IRepoSuscripciones
from app.domain.errors import ClienteNoEncontrado, FondoNoEncontrado

class SubscriptionService:
    def __init__(self, repo_clientes: IRepoClientes, repo_fondos: IRepoFondos, repo_suscripciones: IRepoSuscripciones):
        self.repo_clientes = repo_clientes
        self.repo_fondos = repo_fondos
        self.repo_suscripciones = repo_suscripciones

    def suscribir(self, cliente_id: str, fondo_id: str):
        cliente = self.repo_clientes.get_by_id(cliente_id)
        if not cliente:
            raise ClienteNoEncontrado("Cliente no encontrado")

        fondos = self.repo_fondos.listar()
        if not any(f.id == fondo_id for f in fondos):
            raise FondoNoEncontrado("Fondo no encontrado")

        suscripcion = Suscripcion(cliente_id=cliente_id, fondo_id=fondo_id)
        self.repo_suscripciones.crear(suscripcion)
        return suscripcion
