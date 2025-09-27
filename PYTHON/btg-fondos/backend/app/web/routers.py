from fastapi import APIRouter, Depends
from app.web.schemas import SuscripcionRequest, SuscripcionResponse
from app.adapters.mongo.repo_fondos import RepoFondosMongo   


router = APIRouter(prefix="/api", tags=["Fondos"])

@router.get("/fondos")
def listar_fondos():
    repo = RepoFondosMongo()
    return repo.listar_fondos()

@router.post("/suscribir", response_model=SuscripcionResponse)
def suscribir(req: SuscripcionRequest):
    return {"cliente_id": req.cliente_id, "fondo_id": req.fondo_id}
