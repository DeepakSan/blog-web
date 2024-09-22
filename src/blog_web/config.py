import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    API_KEY = os.environ.get('API_KEY')
    AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID')
    AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')
    AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')