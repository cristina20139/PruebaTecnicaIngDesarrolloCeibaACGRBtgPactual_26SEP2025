"""
Módulo de generación e inserción de fondos en MongoDB.

Este módulo define una lista de fondos de inversión simulados
y los inserta en la colección `fondos` de la base de datos `btg_fondos`.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27, Bogotá D.C., Colombia
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# 🚨 Usa tu cadena de conexión (o desde config/.env)
uri = "mongodb+srv://auragarzonr_db_user:Prueba123@cluster0.lkdpmah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi("1"))
db = client["btg_fondos"]          # nombre de tu base de datos
fondos_collection = db["fondos"]   # colección fondos

fondos = [
    {
        "_id": 1,
        "nombre": "FPV_BTG_PACTUAL_RECAUDADORA",
        "monto_minimo": 75000,
        "categoria": "FPV"
    },
    {
        "_id": 2,
        "nombre": "FPV_BTG_PACTUAL_ECOPETROL",
        "monto_minimo": 125000,
        "categoria": "FPV"
    },
    {
        "_id": 3,
        "nombre": "DEUDAPRIVADA",
        "monto_minimo": 50000,
        "categoria": "FIC"
    },
    {
        "_id": 4,
        "nombre": "FDO-ACCIONES",
        "monto_minimo": 250000,
        "categoria": "FIC"
    },
    {
        "_id": 5,
        "nombre": "FPV_BTG_PACTUAL_DINAMICA",
        "monto_minimo": 100000,
        "categoria": "FPV"
    }
]

try:
    # Limpia colección antes de insertar para evitar duplicados
    fondos_collection.delete_many({})
    fondos_collection.insert_many(fondos)
    print("✅ Fondos insertados correctamente en MongoDB")
except Exception as e:
    print("❌ Error insertando fondos:", e)
