from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from .models import User

def get_all_users(session: Session):
    stmt = select(User).order_by(User.id)
    return session.scalars(stmt).all()

def get_user_by_username(session: Session, username: str):
    stmt = select(User).where(User.username == username)
    return session.scalars(stmt).first()

def create_user(session: Session, username: str, email: str, full_name: str = None):
    user = User(username=username, email=email, full_name=full_name)
    session.add(user)
    try:
        session.commit()
        session.refresh(user)
        return user
    except IntegrityError:
        session.rollback()
        print("Error: username or email already exists.")

def update_user(session: Session, username: str, **kwargs):
    stmt = update(User).where(User.username == username).values(**kwargs)
    session.execute(stmt)
    session.commit()
