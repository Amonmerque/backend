# __init__.py File
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from sqlalchemy import MetaData
from config import Config
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://neondb_owner:npg_0b5hXqkCUHtu@ep-old-mountain-a25cfcsg-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require"
app.config['SECRET_KEY'] = "npg_0b5hXqkCUHtu"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

metadata = MetaData(
 naming_convention={
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
 }
)

db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)  

# Instantiate REST API
api = Api(app)

from api import models, routes