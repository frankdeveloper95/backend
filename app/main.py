from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.main import api_router


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME,
    generate_unique_id_function=custom_generate_unique_id,
)

if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
# class LoginRequest(BaseModel):
#     email: str
#     password: str

# @app.post("/login")
# async def login(request: LoginRequest):
#     with Session(engine) as session:
#         user = crud.get_user_by_email(session=session, email=request.email)
#     if user is not None:
#         is_password_valid = verify_password(plain_password=request.password, hashed_password=user.password)
#         if not is_password_valid:
#             raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Contrasena incorrecta")
#         if is_password_valid:
#             return {"message": "Login successful"}
#         else:
#             return {"message": "Login failed"}
#     else:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email no registrado")
