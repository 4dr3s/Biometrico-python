import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://root:12345@localhost/biometrico')
    SQLALCHEMY_TRACK_MODIFICATIONS = False