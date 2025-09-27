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
from app.web.schemas import SuscripcionRequest, SuscripcionResponse, FondoRequest, FondoResponse
from app.adapters.mongo.repo_clientes import RepoClientesMongo
from app.adapters.mongo.repo_fondos import RepoFondosMongo
from app.adapters.mongo.repo_suscripciones import RepoSuscripcionesMongo
from app.adapters.mongo.repo_transacciones import RepoTransaccionesMongo
from app.services.fondos_service import FondosService
from app.services.clientes_service import ClientesService
from app.services.suscripciones_service import SubscripcionService
from app.services.transacciones_service import TransaccionesService
from app.services.saldo_service import SaldoService

from app.domain.errors import ClienteNoEncontrado, FondoNoEncontrado



router = APIRouter(prefix="/api", tags=["Fondos y Clientes"])

# Repositorios
repo_clientes = RepoClientesMongo()
repo_fondos = RepoFondosMongo()
repo_suscripciones = RepoSuscripcionesMongo()
repo_trasancciones = RepoTransaccionesMongo()
transacciones_service = TransaccionesService(repo_trasancciones)
saldo_service = SaldoService(repo_clientes, repo_suscripciones)

fondos_service = FondosService(repo_fondos)
subscription_service = SubscripcionService(repo_clientes, repo_fondos, repo_suscripciones,repo_trasancciones)
clientes_service = ClientesService(repo_clientes)



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
    # Llama al servicio en vez de al repositorio
    clientes = clientes_service.listar_clientes()
    return clientes  # ya son dicts, no necesitas .dict()


@router.get("/clientes/{cliente_id}", summary="Obtener cliente por ID")
def obtener_cliente(cliente_id: int):
    """
    Endpoint para obtener un cliente por su ID.

    Args:
        cliente_id (int): Identificador del cliente.

    Raises:
        HTTPException: Si el cliente no existe.

    Returns:
        dict: Información del cliente encontrado.
    """
    cliente = clientes_service.obtener_cliente(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.get("/transacciones", summary="Consultar historial de transacciones")
def historial_transacciones(cliente_id: int):
    """
    Endpoint para consultar el historial de transacciones de un cliente.

    Args:
        cliente_id (int): ID del cliente.

    Raises:
        HTTPException: Si el cliente no tiene transacciones.

    Returns:
        List[dict]: Lista de transacciones (aperturas y cancelaciones).
    """
    transacciones = transacciones_service.listar_transacciones_por_cliente(cliente_id)
    if not transacciones:
        raise HTTPException(status_code=404, detail="No se encontraron transacciones para el cliente")
    return transacciones

@router.get("/saldo", summary="Consultar saldo actual")
def consultar_saldo(cliente_id: int):
    """
    Endpoint para consultar el saldo disponible de un cliente para nuevas suscripciones.

    Args:
        cliente_id (int): ID del cliente.

    Raises:
        HTTPException: Si el cliente no existe.

    Returns:
        dict: Saldo disponible.
    """
    try:
        saldo = saldo_service.obtener_saldo(cliente_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return {"cliente_id": cliente_id, "saldo_disponible": saldo}

@router.post("/fondos", response_model=FondoResponse, summary="Crear un nuevo fondo")
def crear_fondo(request: FondoRequest):
    """
    Endpoint para crear un nuevo fondo.

    Args:
        request (FondoRequest): Datos necesarios para crear el fondo.

    Raises:
        HTTPException: Si el monto mínimo es inválido u ocurre un error en la creación.

    Returns:
        FondoResponse: Fondo creado con su ID.
    """
    try:
        fondo = fondos_service.crear_fondo(
            nombre=request.nombre,
            monto_minimo=request.monto_minimo,
            categoria=request.categoria
        )
        return FondoResponse(**fondo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))