#src/models/__init__.py
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

# initialize our db
from app import app
from app import db

db = SQLAlchemy()
bcrypt = Bcrypt()