from flask import Blueprint

from src.routes.customer_route import customer_bp
from src.utils.wrapper import token_required

subcategory_bp = Blueprint("subcategory_bp", __name__, url_prefix="/subcategory")

@customer_bp.route('/', methods=['POST'])
@token_required
def create(current_user):
    auth = request.authorization
    current_user_phone = auth.get('username')

    try:
        body = request.get_json()
        name = body.get('name', None)

        if Category.check_if_exist(current_user_phone):
            category = Category(name=name)
            return jsonify({
                "success": True,
                "id": category.id,
                "message": f"Catégorie {name} ajoutée avec succès",
                "code": 201
            }, 201)
        else:
            return jsonify({
                "success": False,
                "message": "Le client existe déjà",
                "code": 403
            }, 403)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)
