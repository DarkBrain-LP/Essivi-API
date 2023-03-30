from flask import Blueprint, jsonify

cmd_bp = Blueprint('cmd_bp', __name__, '/command')


@cmd_bp.route('/', methods=['POST'])
def create():
    # return success message
    return jsonify({
        "message": "success"
    })
