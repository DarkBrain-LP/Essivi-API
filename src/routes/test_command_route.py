from flask import jsonify, Blueprint

commandtest_bp = Blueprint('commandtest_bp', __name__, '/commandtest')

@commandtest_bp.route('/', methods=['POST'])
def create():
    # return success message
    return jsonify({
        "message": "success"
    })