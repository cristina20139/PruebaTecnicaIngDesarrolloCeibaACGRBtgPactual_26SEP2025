"""
Módulo de conexión a MongoDB.

Este módulo permite conectarse a la base de datos 'btg_fondos'
utilizada en la aplicación de gestión de fondos.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
"""

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# URI de conexión a MongoDB
MONGO_URI = os.getenv("MONGO_URI")

def get_database():
    """
    Obtiene la base de datos 'btg_fondos' desde MongoDB.

    Esta función crea un cliente MongoDB utilizando la URI
    configurada en las variables de entorno y retorna el objeto
    de base de datos correspondiente.

    Returns:
        pymongo.database.Database: Objeto de la base de datos 'btg_fondos'.

    Raises:
        pymongo.errors.ConnectionError: Si no se puede establecer conexión con MongoDB.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27 04:37 GMT-5, Bogotá D.C., Colombia
    """
    client = MongoClient(MONGO_URI)
    return client["btg_fondos"]  # 👈 asegúrate que el nombre es correcto
