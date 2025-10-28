from fastapi import APIRouter

from app.api.routes import login, users, operadora

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(operadora.router)