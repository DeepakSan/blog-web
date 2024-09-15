import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    API_KEY = os.environ.get('API_KEY')