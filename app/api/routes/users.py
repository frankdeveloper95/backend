from fastapi import APIRouter

from app.api.deps import SessionDep
from app.core.security import get_password_hash
from app.models import User, UserCreate, AddUserResponse

router = APIRouter(tags=["users"])


@router.post("/users", response_model=AddUserResponse)
async def add_user(user: UserCreate, session: SessionDep):
    db_user = User.model_validate(user, update={"hashed_password": get_password_hash(user.password)})
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return {"message": "Usuario Anadido", "user": db_user}
