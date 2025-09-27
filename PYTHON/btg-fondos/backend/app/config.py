"""
Configuración de la aplicación usando Pydantic Settings.

Este módulo define la configuración principal de la aplicación,
incluyendo la URI de MongoDB y el nombre de la base de datos. 
Permite cargar valores desde variables de entorno o un archivo .env.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27, Bogotá D.C., Colombia
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Clase de configuración de la aplicación.

    Attributes:
        mongo_uri (str): URI de conexión a MongoDB.
        mongo_db (str): Nombre de la base de datos de la aplicación.
    """

    mongo_uri: str = "mongodb+srv://auragarzonr_db_user:Prueba123@cluster0.lkdpmah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    mongo_db: str = "btg_db"

    class Config:
        """
        Configuración interna de Pydantic Settings.

        Permite cargar variables desde un archivo .env.
        """
        env_file = ".env"


# Instancia de configuración
settings = Settings()
