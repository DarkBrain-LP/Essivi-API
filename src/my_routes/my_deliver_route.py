from flask import Blueprint, jsonify

from src.models.deliver import Deliver

deli_bp = Blueprint('deli_bp', __name__, '/deliver')

@deli_bp.route('/', methods=['GET'])
def get_all():
    delivers = [deliv.format() for deliv in Deliver.query.all()]
    return jsonify({
        "success": True,
        "result": delivers
    })

