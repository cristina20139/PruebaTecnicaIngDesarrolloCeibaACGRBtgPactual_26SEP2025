class TransaccionService:
    def __init__(self, repo_clientes, repo_fondos, repo_suscripciones):
        self.repo_clientes = repo_clientes
        self.repo_fondos = repo_fondos
        self.repo_suscripciones = repo_suscripciones

    def consultar_historial(self, cliente_id: str):
        """
        Consulta todas las transacciones de un cliente incluyendo
        información completa del cliente y del fondo.
        """
        cliente = self.repo_clientes.obtener_cliente_por_id(cliente_id)
        if not cliente:
            raise ClienteNoEncontrado(f"Cliente {cliente_id} no encontrado")

        transacciones = self.repo_suscripciones.listar_por_cliente(cliente_id)
        fondos = {f["id"]: f for f in self.repo_fondos.listar_fondos()}

        historial = []
        for t in transacciones:
            fondo = fondos.get(t["fondo_id"])
            historial.append({
                "cliente": cliente,
                "fondo": fondo,
                "monto": t["monto"],
                "tipo": t["tipo"],
                "fecha": t["fecha"]
            })

        return historial
