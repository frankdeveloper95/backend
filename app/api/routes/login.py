from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app import crud
from app.core.database import engine
from app.core.security import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.api.deps import get_current_active_user
from app.models import Token, User

router = APIRouter(tags=["login"])


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = crud.authenticate(session=Session(engine), email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")


@router.get("/test", response_model=User)
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
