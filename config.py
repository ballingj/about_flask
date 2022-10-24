import os
basedir = os.path.abspath(os.path.dirname(__file__))


""" 
To test, in the prompt issue or set the SERET_KEY before
starting python
SECRET_KEY = foo python
from microapp import app
app.config['SECRET_KEY']
"""
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

