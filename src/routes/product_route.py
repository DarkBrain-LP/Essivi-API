from flask import Blueprint, request, jsonify

from src.models.product import Product
from src.routes.customer_route import customer_bp
from src.utils.wrapper import token_required

product_bp = Blueprint("product_bp", __name__, url_prefix="/product")

@customer_bp.route('/', methods=['POST'])
@token_required
def create(current_user):
    auth = request.authorization
    current_user_phone = auth.get('username')

    try:
        body = request.get_json()
        name = body.get('name', None)
        volume_litter = body.get('volumeLitter', None)
        price = body.get('price', None)
        number = body.get('number', None)
        category = body.get('category', None)

        if Product.check_if_exist(name):
            product = Product(name=name, volume_litter=volume_litter, price=price, number=number, category=category)
            Product.insert(product)
            return jsonify({
                "success": True,
                "id": product.id,
                "message": f"Produit {name} ajoutée avec succès",
                "code": 201
            }, 201)
        else:
            return jsonify({
                "success": False,
                "message": "Le produit existe déjà",
                "code": 403
            }, 403)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)
