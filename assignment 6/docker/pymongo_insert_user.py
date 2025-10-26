from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
uri = "mongodb://app_user:app_password@localhost:27017/appdb?authSource=appdb"
client = MongoClient(uri)
db = client["appdb"]
users = db["users"]

# Function to create a user document
def create_user():
    user_doc = {
        "email": "bob@example.com",
        "name": {"first": "Bob", "last": "Brown"},
        "profile": {
            "dob": datetime(1995, 5, 22),
            "phone": "+49 176 9876543",
            "address": {
                "line1": "Poststraße 5",
                "city": "Hamburg",
                "postal_code": "20095",
                "country": "DE"
            },
            "preferences": {
                "newsletter": False,
                "languages": ["en"]
            }
        },
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

    result = users.insert_one(user_doc)
    print(f"✅ User inserted with _id: {result.inserted_id}")

if __name__ == "__main__":
    create_user()
