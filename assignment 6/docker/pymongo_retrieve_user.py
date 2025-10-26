from pymongo import MongoClient

# MongoDB connection
uri = "mongodb://app_user:app_password@localhost:27017/appdb?authSource=appdb"
client = MongoClient(uri)
db = client["appdb"]
users = db["users"]

# Function to retrieve user by email
def get_user_by_email(email):
    user = users.find_one({"email": email}, {"_id": 0})  # exclude ObjectId for clarity
    if user:
        print(f"✅ User found for {email}:")
        print(user)
    else:
        print(f"❌ No user found for {email}")

# Function to retrieve users by city
def get_users_by_city(city):
    results = users.find({"profile.address.city": city}, {"_id": 0, "email": 1, "name": 1})
    print(f"✅ Users living in {city}:")
    for user in results:
        print(user)

if __name__ == "__main__":
    get_user_by_email("bob@example.com")
    print()
    get_users_by_city("Hamburg")
