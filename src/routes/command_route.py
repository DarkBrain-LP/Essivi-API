# add command_bp that will be used to manage the command
from flask import Blueprint, request, jsonify, abort
from src.models.command import Command
from src.models.command_product import CommandProduct

command_bp = Blueprint("command_bp", __name__, url_prefix="/command")

# add a command and its products and quantities to the database
@command_bp.route("/add", methods=["POST"])
def add_command():
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
    # add the command to the database
    command = Command(command['customer'], command['deliverer'], command['deliveryPoint'], command['status'],
                      command['date'])
    command.insert()
    # add the products to the database
    for product in products:
        command_product = CommandProduct(command.id, product['product'], product['quantity'])
        command_product.insert()
    # return the json format of the command
    return jsonify({
        'status': 'success',
        'command': command.format()
    }), 200