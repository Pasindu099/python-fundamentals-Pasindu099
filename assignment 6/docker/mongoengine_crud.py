import mongoengine as me
from datetime import datetime
from models import User, Profile, Address, Preferences

# Connect to database
me.connect(
    db="appdb",
    username="app_user",
    password="app_password",
    host="localhost",
    port=27017,
    authentication_source="appdb"
)

# Function to create a user
def create_user():
    # Prevent duplicate key errors by deleting existing user
    User.objects(email="charlie@example.com").delete()

    address = Address(
        line1="Musterstraße 10",
        city="Berlin",
        postal_code="10115",
        country="DE"
    )
    prefs = Preferences(newsletter=True, languages=["en", "de"])
    profile = Profile(
        dob=datetime(1998, 10, 26),
        phone="+49 170 3334455",
        address=address,
        preferences=prefs
    )

    user = User(
        email="charlie@example.com",
        name={"first": "Charlie", "last": "Schmidt"},
        profile=profile
    )
    user.save()
    print("✅ User created successfully with MongoEngine!")

# Function to retrieve all users
def retrieve_users():
    print("📋 List of Users:")
    for user in User.objects:
        print(f"- {user.name['first']} ({user.email})")

# Function to update user
def update_user(email):
    user = User.objects(email=email).first()
    if user:
        if "fr" not in user.profile.preferences.languages:
            user.profile.preferences.languages.append("fr")
        user.profile.phone = "+49 176 8889990"
        user.updated_at = datetime.utcnow()
        user.save()
        print(f"✅ User '{email}' updated successfully!")
    else:
        print("❌ User not found.")

if __name__ == "__main__":
    create_user()
    retrieve_users()
    update_user("charlie@example.com")
