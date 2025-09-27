from fastapi import FastAPI
from app.web import routers

def create_app() -> FastAPI:
    app = FastAPI(title="BTG Fondos API", version="1.0.0")
    app.include_router(routers.router)
    return app

app = create_app()