from flask import Blueprint, jsonify, request

from src import db
from src.models.command import Command
from src.models.command_product import CommandProduct
from src.models.deliver import Deliver

my_cmd_bp = Blueprint('my_cmd_bp', __name__, url_prefix='/mycmd')

# get all commands
@my_cmd_bp.route("/", methods=["GET"])
def get_commands():
    try:
        # get all commands from the database
        commands = Command.query.all()
        # return the json format of the commands
        return jsonify({
            'status': 'success',
            'commands': [command.format() for command in commands]
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)


# add a command and its products and quantities to the database
@my_cmd_bp.route("/", methods=["POST"])
def add_command(current_user):
    try:
        # make control on the request boby elements. Check also if they are null or are already in the database
        # if request.json is None or "customer" not in request.json or "deliverer" not in request.json or "deliveryPoint" not in request.json or "status" not in request.json or "date" not in request.json or "products" not in request.json:
        #     abort(400, "Invalid request body")
        # if Command.get_by_customer(request.json["customer"]) is not None:
        #     abort(400, "Customer already exists")
        # if Command.get_by_deliverer(request.json["deliverer"]) is not None:
        #     abort(400, "Deliverer already exists")
        # if Command.get_by_delivery_point(request.json["deliveryPoint"]) is not None:
        #     abort(400, "Delivery point already exists")
        # if Command.get_by_status(request.json["status"]) is not None:
        #     abort(400, "Status already exists")
        # if Command.get_by_date(request.json["date"]) is not None:
        #     abort(400, "Date already exists")
        # if Command.get_by_products(request.json["products"]) is not None:
        #     abort(400, "Products already exists")
        #

        # get the json data from the request
        data = request.get_json()
        # get the command from the data
        command = data['command']
        # get the products and quantities from the data
        products = data['products']

        # check if connected user is deliverer
        deliverer = Deliver.query.filter_by(id=current_user.id).first()
        if deliverer is None:
            deliverer = command['deliverer']
        # customer = Customer.query.filter_by(id=current_user.id).first()
        # if customer is None:
        customer = command['customer']  # , command['deliverer']

        # add the command to the database
        command = Command(customer=customer, deliverer=deliverer, delivery_point=command['deliveryPoint'])
        db.session.add(command)
        db.session.commit()
        # Command.insert(command)
        # add the products to the database
        for product in products:
            command_product = CommandProduct(command.id, product['id'], product['quantity'])
            # db.session.
            CommandProduct.insert(command_product)
        # return the json format of the command
        return jsonify({
            'status': 'success',
            'command': command.format()
        }), 201
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Veuillez entrer toutes les données"
        }, 400)