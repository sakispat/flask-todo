from os import path, environ
from dotenv import load_dotenv


BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, '.env'))


class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('TRACK_MODIFICATIONS')
