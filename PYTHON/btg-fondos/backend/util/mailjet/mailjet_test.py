from mailjet_rest import Client
import os

# Opcional: cargar las credenciales desde variables de entorno
API_KEY = os.environ.get('MJ_APIKEY_PUBLIC', 'TU_API_KEY')
API_SECRET = os.environ.get('MJ_APIKEY_PRIVATE', 'TU_SECRET_KEY')

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

def enviar_correo(destinatario_email, destinatario_nombre, asunto, mensaje):
    data = {
      'Messages': [
        {
          "From": {
            "Email": "tu_correo@dominio.com",
            "Name": "BTG Pactual"
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
    
    result = mailjet.send.create(data=data)
    if result.status_code == 200:
        print("Correo enviado correctamente")
    else:
        print("Error al enviar correo:", result.status_code, result.json())
