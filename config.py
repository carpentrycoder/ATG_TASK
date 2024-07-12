import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MAHESH_7738544966'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
