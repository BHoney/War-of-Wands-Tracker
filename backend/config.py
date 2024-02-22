import os
basedir = os.path.abspath(os.path.dirname(__file__))

class configuration():
    SECRET_KEY = os.environ.get('Secret Key') or 'Secret-Key'
    SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, "app.db")