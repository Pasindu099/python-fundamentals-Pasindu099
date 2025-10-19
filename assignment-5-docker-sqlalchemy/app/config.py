import os

# Database credentials (same as docker-compose.yml)
DB_USER = os.getenv("DB_USER", "app_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "app_password")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "app_db")

# SQLAlchemy database URL
SQLALCHEMY_DATABASE_URL = (
    f"mariadb+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Connection pool settings
POOL_SIZE = 5
MAX_OVERFLOW = 10
POOL_RECYCLE = 1800
POOL_PRE_PING = True
