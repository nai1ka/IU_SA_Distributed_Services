import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://softarch:123456@localhost/twitter2')
    SQLALCHEMY_TRACK_MODIFICATIONS = False