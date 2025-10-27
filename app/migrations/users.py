from passlib.context import CryptContext
from sqlmodel import Session, select

from app.core.database import engine
from app.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user():
    with Session(engine) as session:
        existing_user = session.exec(select(User).where(User.email == "test@example.com")).first()
        if not existing_user:
            test_user = User(email="test@example.com", password=pwd_context.hash("password"))
            session.add(test_user)
            session.commit()


def main():
    create_user()


if __name__ == "__main__":
    main()
