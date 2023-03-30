from flask import Blueprint, request, jsonify

from src import db
from src.models.product import Product
from src.routes.customer_route import customer_bp
from src.utils.wrapper import token_required

from flask import Blueprint, jsonify

prod_bp = Blueprint('prod_bp', __name__, url_prefix='/product')


# @prod_bp.route('/', methods=['POST'])
# def add():
#     return jsonify({
#         "message": "success"
#     })

@prod_bp.route('/', methods=['POST'])
@token_required
def create(current_user):
    # auth = request.authorization
    # current_user_phone = auth.get('username')

    try:
        body = request.get_json()
        name = body.get('name', None)
        volume_litter = body.get('volumeLitter', None)
        price = body.get('price', None)
        number = body.get('number', None)
        category = body.get('category', None)

        if not Product.check_if_exist(name):
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


@prod_bp.route('/<int:id>', methods=['PATCH'])
@token_required
def update(current_user, id):
    # auth = request.authorization
    # current_user_phone = auth.get('username')

    try:
        product = Product.query.get(id)
        if product is not None:
            body = request.get_json()
            name = body.get('name', None)
            volume_litter = body.get('volumeLitter', None)
            price = body.get('price', None)
            number = body.get('number', None)
            category = body.get('category', None)

            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if category is not None:
                product.category = category
            if number is not None:
                product.number = number
            if volume_litter is not None:
                product.volume_litter = volume_litter

            Product.update()
            # db.session.commit()
            return jsonify({
                "success": True,
                "id": product.id,
                "product": product.format(),
                "message": f"Produit {name} ajoutée avec succès",
                "code": 201
            }, 201)
            # else:
            #     return jsonify({
            #         "success": False,
            #         "message": "Le produit existe déjà",
            #         "code": 403
            #     }, 403)

        else:
            return jsonify({
                "success": False,
                "message": "Le produit n'existe pas",
                "code": 403
            }, 403)

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)
