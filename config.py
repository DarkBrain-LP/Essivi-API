import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'essivi.db')

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'my_precious'
