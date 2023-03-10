from datetime import datetime

from flask import request, Blueprint, jsonify
from werkzeug.security import generate_password_hash

from src.models import deliver
from src.models.deliver import Deliver
from src.models.person import Person
from src.utils.wrapper import token_required

deliver_bp = Blueprint("deliver_bp", __name__, url_prefix='/deliver')

@deliver_bp.route('/', methods=['POST'])
@token_required
def create(current_user):
    # try catch
    try:
        body = request.get_json()
        name = body.get('name', None)
        fname = body.get('firstname', None)
        phone = body.get('phone', None)
        password = body.get('password', None)
        quarter = body.get('quarter', None)
        hire_date = body.get('hireDate', None)
        hire_date = datetime.strptime(hire_date, "%d-%m-%Y").date()
        # TODO: check if the deliver already exists

        # hash password
        password = generate_password_hash(password)
        deliver = Deliver(name=name, firstname=fname, phone=phone, password=password, quarter=quarter, hire_date=hire_date)
        if deliver is None:
            return jsonify({
                "success": False,
                "message": "Bad Request"
            }, 400)

        # check if deliver already exists
        if Deliver.check_if_exist(phone):
            return jsonify({
                "success": False,
                "message": "Deliver already exists"
            }, 400)
        else:
            deliver.insert()
            return jsonify({
                "success": True,
                "message": "Deliver created successfully"
            }, 201)
    except Exception as e:
        deliver_ = Deliver(name=name, firstname=fname, phone=phone, quarter=quarter, hire_date=hire_date)
        return jsonify({
            "success": False,
            "message": str(e) + "Bad Request"
        }, 400)

