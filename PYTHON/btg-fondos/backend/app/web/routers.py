"""
Módulo de enrutamiento FastAPI para la gestión de fondos y clientes.

Este módulo define los endpoints para listar fondos, suscribirse a un fondo,
listar clientes y obtener un cliente por ID. Se encarga de la coordinación
entre los repositorios y la exposición de la API REST.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27, Bogotá D.C., Colombia
"""

from fastapi import APIRouter, HTTPException
from app.web.schemas import SuscripcionRequest, SuscripcionResponse
from app.adapters.mongo.repo_clientes import RepoClientesMongo
from app.adapters.mongo.repo_fondos import RepoFondosMongo
from app.adapters.mongo.repo_suscripciones import RepoSuscripcionesMongo
from app.services.suscripciones_service import SubscripcionService
from app.domain.errors import ClienteNoEncontrado, FondoNoEncontrado



router = APIRouter(prefix="/api", tags=["Fondos y Clientes"])

# Repositorios
repo_clientes = RepoClientesMongo()
repo_fondos = RepoFondosMongo()
repo_suscripciones = RepoSuscripcionesMongo()

subscription_service = SubscripcionService(repo_clientes, repo_fondos, repo_suscripciones)



# --- Fondos ---
@router.get("/fondos")
def listar_fondos():
    """
    Endpoint para listar todos los fondos disponibles.

    Returns:
        list: Lista de fondos con sus atributos principales.
    """
    return repo_fondos.listar_fondos()


# --- Suscripción ---
@router.post("/fondos/{fondo_id}/suscribirse", response_model=SuscripcionResponse)
def suscribir(fondo_id: int, req: SuscripcionRequest):
    """
    Endpoint para que un cliente se suscriba a un fondo usando SubscriptionService.

    Args:
        fondo_id (int): ID del fondo al cual se suscribe el cliente.
        req (SuscripcionRequest): Datos de la suscripción (cliente_id, monto).

    Raises:
        HTTPException: Si el cliente o fondo no existen.

    Returns:
        SuscripcionResponse: Información de la suscripción creada.
    """
    try:
        # Llamamos al service, no a los repositorios
        suscripcion = subscription_service.suscribir(
            cliente_id=req.cliente_id,
            fondo_id=fondo_id,
            monto=req.monto
        )
        return SuscripcionResponse(
            cliente_id=suscripcion.cliente_id,
            fondo_id=suscripcion.fondo_id,
            monto=suscripcion.monto,
            tipo=suscripcion.tipo,
            fecha=suscripcion.fecha
        )
    except ClienteNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))
    except FondoNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))

# --- Clientes ---
@router.get("/clientes", summary="Listar todos los clientes")
def listar_clientes():
    """
    Endpoint para listar todos los clientes registrados.

    Returns:
        list: Lista de clientes con sus atributos principales.
    """
    return repo_clientes.listar_clientes()


@router.get("/clientes/{cliente_id}", summary="Obtener cliente por ID")
def obtener_cliente(cliente_id: int):
    """
    Endpoint para obtener un cliente por su ID.

    Args:
        cliente_id (str): Identificador del cliente.

    Raises:
        HTTPException: Si el cliente no existe.

    Returns:
        dict: Información del cliente encontrado.
    """
    cliente = repo_clientes.obtener_cliente_por_id(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente
