from functools import wraps

import jwt
from flask import Flask, request, jsonify

from config import SECRET_KEY
from src.extension import db, migrate
from src.models.person import Person
from src.routes.authRoute import auth_bp
from src.routes.deliverRoute import deliver_bp



def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    app.register_blueprint(deliver_bp)
    app.register_blueprint(auth_bp)

    return app