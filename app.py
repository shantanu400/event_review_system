# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import routes after initializing app to prevent circular imports
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
