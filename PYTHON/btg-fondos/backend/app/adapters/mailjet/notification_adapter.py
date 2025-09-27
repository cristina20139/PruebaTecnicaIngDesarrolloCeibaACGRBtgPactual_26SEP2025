# adapters/notification_adapter.py
from services.notification_service import NotificacionService

class NotificacionAdapter:
    """
    Adaptador para exponer el servicio de notificaciones a la capa de aplicación.
    """

    def __init__(self, notificacion_service: NotificacionService):
        self.notificacion_service = notificacion_service

    def enviar(self, email: str, nombre: str, asunto: str, mensaje: str):
        return self.notificacion_service.enviar_email(email, nombre, asunto, mensaje)
