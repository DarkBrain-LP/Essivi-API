from flask import Blueprint, request, jsonify

from src import db
from src.models.category import Category
from src.models.subcategory import SubCategory
from src.routes.customer_route import customer_bp
from src.utils.wrapper import token_required

category_bp = Blueprint("category_bp", __name__, url_prefix="/category")


@customer_bp.route('/', methods=['POST'])
@token_required
def create(current_user):
    auth = request.authorization
    current_user_phone = auth.get('username')

    try:
        body = request.get_json()
        name = body.get('name', None)

        if not Category.check_if_exist(name):
            category = Category(name=name)
            db.session.add(category)
            db.session.commit()
            return jsonify({
                "success": True,
                "id": category.id,
                "message": f"Catégorie {name} ajoutée avec succès",
                "code": 201
            }, 201)
        else:
            return jsonify({
                "success": False,
                "message": "La catégorie existe déjà",
                "code": 403
            }, 403)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)


@customer_bp.route('/<int:id>/subcategory', methods=['POST'])
@token_required
def addSubcategory(current_user, id: int):
    auth = request.authorization
    current_user_phone = auth.get('username')

    try:
        body = request.get_json()
        name = body.get('name', None)

        category = Category.query.filter_by(id=id)
        if category is None:

            if not SubCategory.check_if_exist(id, name):
                scategory = SubCategory(name=name, category_id=id)
                db.session.add(scategory)
                return jsonify({
                    "success": True,
                    "id": scategory.id,
                    "message": f"Catégorie {name} ajoutée avec succès",
                    "code": 201
                }, 201)

            else:
                return jsonify({
                    "success": False,
                    "message": "Cette sous-catégorie existe déjà pour cette catégorie",
                    "code": 403
                }, 403)
        else:
            return jsonify({
                "success": False,
                "message": "Cette catégorie n'existe pas",
                "code": 404
            }, 404)

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)


@customer_bp.route('/<int:id>/updateState/<int:state>', methods=['GET'])
@token_required
def update(current_user, id: int, state: int):
    """

    :param id: the category id
    :param state: 0 -> activate | 1 -> deactivate
    :param current_user: the connected user
    :return:
    """
    auth = request.authorization
    current_user_phone = auth.get('username')

    try:
        body = request.get_json()

        if Category.check_if_id_exist(id):
            category = Category.query.get(id)
            category.is_active = state
            Category.update()
            return jsonify({
                "success": True,
                "id": category.id,
                "message": f"Etat changé",
                "code": 202
            }, 202)
        else:
            return jsonify({
                "success": False,
                "message": "La catégorie n'existe pas",
                "code": 403
            }, 403)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)
