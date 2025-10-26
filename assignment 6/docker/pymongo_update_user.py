from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
uri = "mongodb://app_user:app_password@localhost:27017/appdb?authSource=appdb"
client = MongoClient(uri)
db = client["appdb"]
users = db["users"]

# Function to update user preferences and phone number
def update_user(email):
    result = users.update_one(
        {"email": email},
        {
            "$set": {
                "profile.phone": "+49 175 2223344",
                "profile.preferences.newsletter": True,
                "updated_at": datetime.utcnow()
            },
            "$addToSet": {"profile.preferences.languages": "fr"}
        }
    )

    if result.modified_count > 0:
        print(f"✅ User '{email}' updated successfully.")
    else:
        print(f"⚠️ No matching user found or no changes applied.")

# Function to verify updated document
def verify_update(email):
    user = users.find_one({"email": email}, {"_id": 0, "email": 1, "profile": 1})
    print("📄 Updated user document:")
    print(user)

if __name__ == "__main__":
    update_user("bob@example.com")
    verify_update("bob@example.com")
