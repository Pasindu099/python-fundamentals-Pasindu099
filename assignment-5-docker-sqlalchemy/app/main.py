from app.db import SessionLocal, engine
from app.models import Base
from app.crud import get_all_users, get_user_by_username, create_user, update_user

def run_demo():
    Base.metadata.create_all(bind=engine)  # ensures table exists

    with SessionLocal() as session:
        print("\n== All Users ==")
        for u in get_all_users(session):
            print(u.id, u.username, u.email, u.full_name)

        print("\n== Find Alice ==")
        user = get_user_by_username(session, "alice")
        print(user.id, user.username, user.email)

        print("\n== Insert Diana ==")
        create_user(session, "diana", "diana@example.com", "Diana Doe")

        print("\n== Update Bob ==")
        update_user(session, "bob", full_name="Robert Brown")

        print("\n== Final Users ==")
        for u in get_all_users(session):
            print(u.id, u.username, u.email, u.full_name)

if __name__ == "__main__":
    run_demo()