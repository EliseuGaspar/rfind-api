from flask import Flask
from flask_cors import CORS
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from os import getenv


load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{getenv('user')}:{getenv('pwd')}@{getenv('host')}/{getenv('db')}"
app.config['JWT_SECRET_KEY'] = getenv('secret_key')
#app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 20
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
CORS(app)
