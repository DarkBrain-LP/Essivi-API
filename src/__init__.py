from functools import wraps

from flask_cors import CORS
import jwt
from flask import Flask, request, jsonify

from config import SECRET_KEY
from src.extension import db, migrate
# from src.models.category import Category
# from src.models.command import Command
# from src.models.command_product import CommandProduct
# from src.models.customer import Customer
# from src.models.delivery_point import DeliveryPoint
# from src.models.person import Person
# from src.models.product import Product
# from src.models.subcategory import SubCategory

from src.routes.auth_route import auth_bp
from src.routes.category_route import category_bp
from src.routes.command_new_route import cmd_bp
# from src.routes.category_route import category_bp
from src.routes.command_route import command_bp
from src.routes.customer_route import customer_bp
from src.routes.deliverRoute import deliver_bp
from src.routes.product_new_route import prod_bp
from src.routes.product_route import product_bp
from src.routes.subcategory_route import subcategory_bp
from src.routes.test_cmd_route import testcmd_bp
from src.routes.test_command_route import commandtest_bp
from src.routes.test_route import test_bp


def create_app():
    app = Flask(__name__)
    CORS(app, origins='*')
    app.config.from_object('config')

    # from src.routes.category_route import category_bp
    # app.register_blueprint(category_bp)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    # from src.models.category import Category
    # from src.models.command import Command
    # from src.models.command_product import CommandProduct
    # from src.models.customer import Customer
    # from src.models.delivery_point import DeliveryPoint
    # from src.models.person import Person
    # from src.models.product import Product
    # from src.models.subcategory import SubCategory

    # app.register_blueprint(category_bp)
    # app.register_blueprint(subcategory_bp)
    # app.register_blueprint(product_bp)
    # app.register_blueprint(command_bp)
    # app.register_blueprint(deliver_bp)

    app.register_blueprint(testcmd_bp)
    app.register_blueprint(commandtest_bp)
    app.register_blueprint(cmd_bp)
    app.register_blueprint(prod_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(test_bp)
    app.register_blueprint(auth_bp)
    # app.register_blueprint(customer_bp)

    return app
