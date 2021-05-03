from flask import Flask
from .config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
obj = Config
if obj.SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    obj.SQLALCHEMY_DATABASE_URI = obj.SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
app.config.from_object(obj)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views,models