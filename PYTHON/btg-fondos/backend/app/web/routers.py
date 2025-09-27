# app/web/routers.py
from fastapi import APIRouter, HTTPException
from app.web.schemas import SuscripcionRequest, SuscripcionResponse
from app.adapters.mongo.repo_clientes import RepoClientesMongo
from app.adapters.mongo.repo_fondos import RepoFondosMongo
from app.adapters.mongo.repo_suscripciones import RepoSuscripcionesMongo

router = APIRouter(prefix="/api", tags=["Fondos y Clientes"])

# Repositorios
repo_clientes = RepoClientesMongo()
repo_fondos = RepoFondosMongo()
repo_suscripciones = RepoSuscripcionesMongo()

# --- Fondos ---
@router.get("/fondos")
def listar_fondos():
    return repo_fondos.listar_fondos()

@router.post("/fondos/{fondo_id}/suscribirse", response_model=SuscripcionResponse)
def suscribir(fondo_id: int, req: SuscripcionRequest):  # fondo_id como int
    # Verificar cliente
    cliente = repo_clientes.obtener_cliente_por_id(req.cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Verificar fondo
    fondo = repo_fondos.collection.find_one({"_id": fondo_id})  # fondo_id como int
    if not fondo:
        raise HTTPException(status_code=404, detail="Fondo no encontrado")

    # Crear suscripción
    suscripcion = repo_suscripciones.crear(
        cliente_id=req.cliente_id,
        fondo_id=fondo_id,
        monto=req.monto
    )

    return SuscripcionResponse(
        cliente_id=suscripcion["cliente_id"],
        fondo_id=suscripcion["fondo_id"],
        monto=suscripcion["monto"],
        tipo=suscripcion["tipo"],
        fecha=suscripcion["fecha"]
    )

# --- Clientes ---
@router.get("/clientes", summary="Listar todos los clientes")
def listar_clientes():
    return repo_clientes.listar_clientes()

@router.get("/clientes/{cliente_id}", summary="Obtener cliente por ID")
def obtener_cliente(cliente_id: str):
    cliente = repo_clientes.obtener_cliente_por_id(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente
