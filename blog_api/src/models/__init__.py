#src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#######
# existing code remains #
db = SQLAlchemy()
#######
bcrypt = Bcrypt()