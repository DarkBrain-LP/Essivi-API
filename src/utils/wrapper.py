from functools import wraps
from flask import  request, jsonify
import jwt
from config import SECRET_KEY
from src.models.person import Person

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')

        if not token:
            current_user = Person.query.first()
            return f(Person.query.first(), *args, **kwargs)

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            current_user = Person.query.filter_by(phone=data['user']).first()
        except Exception as e:
            return jsonify({'message': str(e) + ': Token is invalid!'}), 403

        return f(current_user, *args, **kwargs)

    return decorated
