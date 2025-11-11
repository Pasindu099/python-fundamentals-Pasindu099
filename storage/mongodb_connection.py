from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DB = os.getenv("MONGO_DB", "pipeline_mongo")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))

connect(db=MONGO_DB, host=MONGO_HOST, port=MONGO_PORT)
print("MongoDB connection established.")
