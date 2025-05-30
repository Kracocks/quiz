from flask import Flask
from flask_cors import CORS
import os.path
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)

def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), p))

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///'+mkpath('../server.db')
)
db = SQLAlchemy(app)

CORS(app)