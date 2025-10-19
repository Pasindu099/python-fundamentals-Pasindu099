from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData, func

# Create MetaData object to hold table definitions
metadata = MetaData()

# Define the 'users' table using SQLAlchemy Core
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(50), unique=True, nullable=False),
    Column("email", String(255), unique=True, nullable=False),
    Column("full_name", String(255)),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
)
