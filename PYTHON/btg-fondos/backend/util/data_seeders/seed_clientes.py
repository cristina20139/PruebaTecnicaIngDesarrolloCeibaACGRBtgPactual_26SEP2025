from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from faker import Faker
import random

# =========================
# Configuración MongoDB
# =========================
MONGO_URI = "mongodb+srv://auragarzonr_db_user:Prueba123@cluster0.lkdpmah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI, server_api=ServerApi("1"))
db = client["btg_fondos"]
clientes_collection = db["clientes"]

# =========================
# Configuración Faker
# =========================
fake = Faker('es_CO')  # Nombres y apellidos en español, formato colombiano

# =========================
# Parámetros de generación
# =========================
NUM_CLIENTES = 500  # Cambia este número según lo que necesites

# =========================
# Generación de clientes
# =========================
clientes = []

for i in range(1, NUM_CLIENTES + 1):
    nombre = fake.first_name()
    apellido = fake.last_name()
    cliente = {
        "_id": i,
        "nombres": nombre,
        "apellidos": apellido,
        "correo_electronico": f"{nombre.lower()}.{apellido.lower()}@example.com",
        "telefono": fake.phone_number(),
        "celular": fake.phone_number(),
        "direccion": fake.address(),
        "saldo": round(random.uniform(500000, 2000000), 2)  # Saldo aleatorio entre 500.000 y 2.000.000 COP
    }
    clientes.append(cliente)

# =========================
# Inserción en MongoDB
# =========================
try:
    # Limpia colección antes de insertar para evitar duplicados
    clientes_collection.delete_many({})
    clientes_collection.insert_many(clientes)
    print(f"✅ {NUM_CLIENTES} clientes insertados correctamente en MongoDB")
except Exception as e:
    print("❌ Error insertando clientes:", e)
