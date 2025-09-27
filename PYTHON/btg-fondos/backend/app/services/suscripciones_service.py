from datetime import datetime
from app.domain.entities import Suscripcion, Transaccion
from app.domain.errors import ClienteNoEncontrado, FondoNoEncontrado

class Suscripcion:
    """
    Representa una suscripción de un cliente a un fondo.

    Attributes:
        cliente_id (str): Identificador del cliente.
        fondo_id (str): Identificador del fondo.
        monto (float): Monto invertido en la suscripción.
        tipo (str): Tipo de operación, por defecto "apertura".
        fecha (str): Fecha y hora de la suscripción en formato ISO.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27, Bogotá D.C., Colombia
    """
    def __init__(self, cliente_id: int, fondo_id: int, monto: float):
        self.cliente_id = cliente_id
        self.fondo_id = fondo_id
        self.monto = monto
        self.tipo = "apertura"
        self.fecha = datetime.now().isoformat()


class SubscripcionService:
    """
    Servicio de suscripciones de fondos.

    Esta clase coordina la lógica de negocio para que un cliente pueda
    suscribirse a un fondo, verificando la existencia de cliente y fondo
    y delegando la persistencia al repositorio correspondiente.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27, Bogotá D.C., Colombia
    """
    def __init__(self, repo_clientes, repo_fondos, repo_suscripciones, repo_transacciones, notificacion_service):
        self.repo_clientes = repo_clientes
        self.repo_fondos = repo_fondos
        self.repo_suscripciones = repo_suscripciones
        self.repo_transacciones = repo_transacciones
        self.notificacion_service = notificacion_service

    def suscribir(self, cliente_id: int, fondo_id: int, monto: float):
        """
        Permite a un cliente suscribirse a un fondo.

        Verifica que el cliente y el fondo existan y crea la suscripción.

        Args:
            cliente_id (str): Identificador del cliente.
            fondo_id (str): Identificador del fondo.
            monto (float): Monto a invertir en la suscripción.

        Raises:
            ClienteNoEncontrado: Si el cliente no existe.
            FondoNoEncontrado: Si el fondo no existe.

        Returns:
            Suscripcion: Objeto con los datos de la suscripción creada.
        """
        cliente = self.repo_clientes.obtener_cliente_por_id(cliente_id)
        if not cliente:
            raise ClienteNoEncontrado(f"Cliente {cliente_id} no encontrado")

        fondos = self.repo_fondos.listar_fondos()
        fondo = next((f for f in fondos if f["id"] == fondo_id), None)
        if not fondo:
            raise FondoNoEncontrado(f"Fondo {fondo_id} no encontrado")

        suscripcion = Suscripcion(cliente_id=cliente_id, fondo_id=fondo_id, monto=monto)
        self.repo_suscripciones.crear(suscripcion)

        # Guardar transacción
        # Crear y guardar transacción
        transaccion = Transaccion(
            cliente_id=cliente_id,
            fondo_id=fondo_id,
            tipo="apertura",
            monto=monto
        )

        # Enviar notificación
        mensaje = f"Hola {cliente['nombre']}, tu suscripción al fondo {fondo['nombre']} fue exitosa."
        self.notificacion_service.enviar_email(
            destinatario_email=cliente['correo'],
            destinatario_nombre=cliente['nombre'],
            asunto="Suscripción a fondo exitosa",
            mensaje=mensaje
        )

        self.repo_transacciones.crear(transaccion)       
        return suscripcion
