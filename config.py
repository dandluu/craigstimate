import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))


load_dotenv(os.path.join(basedir, '.env'))


class Config:
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY')