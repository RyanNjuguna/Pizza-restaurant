import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://localhost/pizza_api")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
