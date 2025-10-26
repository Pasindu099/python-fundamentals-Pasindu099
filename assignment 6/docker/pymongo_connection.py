from pymongo import MongoClient

# MongoDB connection URL
uri = "mongodb://app_user:app_password@localhost:27017/appdb?authSource=appdb"

try:
    # Establish connection
    client = MongoClient(uri)

    # Access the database
    db = client["appdb"]

    # Verify connection
    print("✅ Connected to MongoDB successfully!")

    # List all collections
    print("Collections:", db.list_collection_names())

except Exception as e:
    print("❌ Connection failed:", e)
