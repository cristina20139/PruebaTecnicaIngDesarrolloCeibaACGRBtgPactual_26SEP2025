from mailjet_rest import Client

# 1️⃣ Configura tus credenciales de Mailjet
API_KEY = '022348843a4e83f78e3b321b01407992'       # Reemplaza con tu API Key de Mailjet
API_SECRET = '12e7b7c54094168f01e738f75e166714' # Reemplaza con tu Secret Key de Mailjet

# 2️⃣ Inicializa el cliente de Mailjet
mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

# 3️⃣ Función para enviar correo
def enviar_correo(destinatario_email, destinatario_nombre, asunto, mensaje):
    data = {
      'Messages': [
        {
          "From": {
            "Email": "auragarzonr@gmail.com",  # Reemplaza con un email verificado en Mailjet
            "Name": "Aura Cristina Garzón Rodriguez"
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
        print("✅ Correo enviado correctamente")
    else:
        print("❌ Error al enviar correo:", result.status_code, result.json())

# 4️⃣ Llamada a la función con tus datos de prueba
if __name__ == "__main__":
    enviar_correo(
        destinatario_email="auragarzonr@gmail.com",
        destinatario_nombre="Aura Cristina",
        asunto="Suscripción a fondo exitosa",
        mensaje="Hola Aura, tu suscripción al fondo FPV_BTG_PACTUAL_RECAUDADORA fue exitosa."
    )
