from functools import wraps

from flask_cors import CORS
import jwt
from flask import Flask, request, jsonify

from config import SECRET_KEY
from src.extension import db, migrate
from src.my_routes.my_command_route import my_cmd_bp
from src.my_routes.my_deliver_route import deli_bp
from src.my_routes.my_product_route import mycat_bp

from src.routes.auth_route import auth_bp
from src.routes.category_route import category_bp
from src.routes.command_route import command_bp
from src.routes.deliverRoute import deliver_bp
from src.routes.product_new_route import prod_bp
from src.routes.product_route import product_bp
from src.routes.subcategory_route import subcategory_bp
from src.routes.test_cmd_route import testcmd_bp
from src.routes.test_route import test_bp


def create_app():
    app = Flask(__name__)
    CORS(app, origins='*')
    app.config.from_object('config')

    # from src.routes.category_route import category_bp
    # app.register_blueprint(category_bp)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    app.register_blueprint(deli_bp)
    app.register_blueprint(mycat_bp)
    app.register_blueprint(my_cmd_bp)
    app.register_blueprint(testcmd_bp)
    app.register_blueprint(prod_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(test_bp)
    app.register_blueprint(auth_bp)

    return app
