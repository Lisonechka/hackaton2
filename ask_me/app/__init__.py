# it will be ran when the package is imported.
# to define every big variable, like the app and the database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
os.system('export FLASK_APP=run.py')