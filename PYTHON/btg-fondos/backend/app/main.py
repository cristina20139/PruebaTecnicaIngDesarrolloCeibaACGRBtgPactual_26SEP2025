"""
Módulo principal de la aplicación FastAPI.

Este módulo crea la instancia principal de FastAPI para la API
de gestión de fondos y clientes, incluyendo los routers definidos
en `app.web.routers`.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27, Bogotá D.C., Colombia

Comando para iniciar

uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.web import routers


def create_app() -> FastAPI:
    """
    Crea y configura la aplicación FastAPI.

    Esta función inicializa la instancia de FastAPI, configura
    el título y la versión de la API, y agrega los routers
    definidos en la aplicación.

    Returns:
        FastAPI: Instancia de la aplicación FastAPI.
    """
    app = FastAPI(title="BTG Fondos API", version="1.0.0")

    # 🔹 Configuración de CORS para permitir llamadas desde React (http://localhost:5173)
    origins = [
        "http://localhost:5173",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,      # o ["*"] si quieres permitir todos
        allow_credentials=True,
        allow_methods=["*"],        # GET, POST, PUT, DELETE, OPTIONS
        allow_headers=["*"],        # permite todos los headers
    )

    # 🔹 Registro de routers
    app.include_router(routers.router)

    return app


# Instancia principal de la aplicación
app = create_app()
