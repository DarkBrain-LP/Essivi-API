from datetime import datetime, timedelta

import jwt
from flask import Blueprint, request, make_response, jsonify
from werkzeug.security import check_password_hash

from config import SECRET_KEY
from src.models.person import Person

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")


# login with token
@auth_bp.route("/login", methods=["POST"])
def login():
    auth = request.authorization

    # get person by phone
    person = Person.get_by_phone(auth.username)
    # verify hash password of the person
    if person is None or not check_password_hash(person.password, auth.password):
        return jsonify({
            'message': 'invalid credentials',
            'WWW-Authenticate': 'Basic realm="Login required!"'
        }), 401

    # generate token
    token = jwt.encode({'user': auth.username, 'exp': datetime.utcnow() + timedelta(minutes=30)},
                       SECRET_KEY)
    return jsonify({
        'status': 'success',
        'token': token
    }), 200

    return jsonify({'message': 'invalid credentials',
                    'WWW-Authenticate': 'Basic realm="Login required!"'}), 401
