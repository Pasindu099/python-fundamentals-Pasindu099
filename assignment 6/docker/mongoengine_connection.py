import mongoengine as me

# Establish MongoEngine connection
me.connect(
    db="appdb",
    username="app_user",
    password="app_password",
    host="localhost",
    port=27017,
    authentication_source="appdb"
)

print("✅ Connected to MongoDB using MongoEngine!")
