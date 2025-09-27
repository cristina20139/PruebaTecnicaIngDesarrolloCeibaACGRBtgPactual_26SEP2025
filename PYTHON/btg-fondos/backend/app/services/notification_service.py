# services/notification_service.py
from mailjet_rest import Client

class NotificacionService:
    """
    Servicio de notificaciones vía email utilizando Mailjet.
    """

    def __init__(self, api_key: str, api_secret: str, remitente_email: str, remitente_nombre: str):
        self.mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        self.remitente_email = remitente_email
        self.remitente_nombre = remitente_nombre

    def enviar_email(self, destinatario_email: str, destinatario_nombre: str, asunto: str, mensaje: str):
        """
        Envía un correo electrónico al cliente.

        Args:
            destinatario_email: Email del destinatario
            destinatario_nombre: Nombre del destinatario
            asunto: Asunto del correo
            mensaje: Contenido del correo (texto y HTML)

        Returns:
            dict: Respuesta de Mailjet
        """
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": self.remitente_email,
                        "Name": self.remitente_nombre
                    },
                    "To": [
                        {
                            "Email": destinatario_email,
                            "Name": destinatario_nombre
                        }
                    ],
                    "Subject": asunto,
                    "TextPart": mensaje,
                    "HTMLPart": f"<h3>{mensaje}</h3>"
                }
            ]
        }

        result = self.mailjet.send.create(data=data)
        if result.status_code == 200:
            return {"status": "success", "message": "Correo enviado correctamente"}
        else:
            return {"status": "error", "code": result.status_code, "detail": result.json()}
