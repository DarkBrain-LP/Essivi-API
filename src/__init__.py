from functools import wraps

from flask_cors import CORS
import jwt
from flask import Flask, request, jsonify

from config import SECRET_KEY
from src.extension import db, migrate
from src.models.person import Person
from src.routes.auth_route import auth_bp
from src.routes.deliverRoute import deliver_bp



def create_app():
    app = Flask(__name__)
    CORS(app, origins='*')
    app.config.from_object('config')

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    app.register_blueprint(deliver_bp)
    app.register_blueprint(auth_bp)

    return app