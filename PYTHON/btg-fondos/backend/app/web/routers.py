from fastapi import APIRouter, Depends, HTTPException
from app.web.schemas import SuscripcionRequest, SuscripcionResponse
from app.adapters.mongo.repo_fondos import RepoFondosMongo
from app.adapters.mongo.repo_clientes import RepoClientesMongo  # nuevo repo para clientes

router = APIRouter(prefix="/api", tags=["Fondos y Clientes"])

# --- Fondos ---
@router.get("/fondos")
def listar_fondos():
    repo = RepoFondosMongo()
    return repo.listar_fondos()

@router.post("/suscribir", response_model=SuscripcionResponse)
def suscribir(req: SuscripcionRequest):
    return {"cliente_id": req.cliente_id, "fondo_id": req.fondo_id}

# --- Clientes ---
@router.get("/clientes", summary="Listar todos los clientes")
def listar_clientes():
    repo = RepoClientesMongo()
    return repo.listar_clientes()

@router.get("/clientes/{cliente_id}", summary="Obtener cliente por ID")
def obtener_cliente(cliente_id: int):
    repo = RepoClientesMongo()
    cliente = repo.obtener_cliente_por_id(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente
