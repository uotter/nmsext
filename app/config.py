import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'devopsdemo_secret_key'

SQLALCHEMY_DATABASE_URI = 'mysql://nmsweb:1234567890@5.71.10.3/nmsweb'
