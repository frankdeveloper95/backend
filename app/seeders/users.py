from faker import Faker
from passlib.context import CryptContext
from sqlmodel import Session

from app.core.database import engine
from app.models import User, Operadora
from app.core.security import get_password_hash

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user():
    fake = Faker()
    with Session(engine) as session:
        for _ in range(10):
            user = User(
                email=fake.email(),
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                hashed_password=get_password_hash("password"),
                rol_id=2,
                estado_id=1,
                telefono=fake.unique.numerify("09########"),
                cedula=fake.unique.numerify("13########")
            )
            session.add(user)
            session.commit()


def main():
    create_user()


if __name__ == "__main__":
    main()
