from app.adapters.mongo.repo_clientes import RepoClientesMongo

class ClientesService:
    def __init__(self):
        self.repo = RepoClientesMongo()

    def listar_clientes(self):
        return self.repo.listar_clientes()

    def obtener_cliente(self, cliente_id):
        return self.repo.obtener_cliente_por_id(cliente_id)
