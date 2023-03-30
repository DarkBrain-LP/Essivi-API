from flask import Blueprint, request, jsonify
from src.utils.wrapper import token_required

testcmd_bp = Blueprint('test_cmd_bp', __name__, url_prefix='/cmd')


@testcmd_bp.route('/add', methods=['POST'])
@token_required
def add(current_user):
    return {
        'message': 'success'
    }