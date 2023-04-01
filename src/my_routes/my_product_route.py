from datetime import datetime, timezone

from flask import Blueprint
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from src import db
from src.models.category import Category
from src.models.deliver import Deliver
from src.models.product import Product
from src.models.subcategory import SubCategory
from src.utils import constants
from src.utils.wrapper import token_required

mycat_bp = Blueprint("mycat_bp", __name__, url_prefix="/mycat")

@mycat_bp.route('/', methods=['GET'])
@token_required
def get_categories(current_user):
    try:
        categories = Category.query.all()
        if categories is None:
            return jsonify({
                "success": False,
                "message": "Aucune catégorie trouvée",
                "code": 404
            }, 404)
        else:
            categories = [category.format() for category in categories]
            return jsonify({
                "success": True,
                "result": categories,
                "code": 200
            }, 200)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)

@mycat_bp.route('/', methods=['POST'])
def create():
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

@mycat_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        body = request.get_json()
        name = body.get('name', None)

        category = Category.query.filter_by(id=id).first()
        if category is None:
            return jsonify({
                "success": False,
                "message": "La catégorie n'existe pas",
                "code": 404
            }, 404)
        else:
            category.name = name
            db.session.commit()
            return jsonify({
                "success": True,
                "message": f"Catégorie {name} modifiée avec succès",
                "code": 200
            }, 200)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)

@mycat_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        category = Category.query.filter_by(id=id).first()
        if category is None:
            return jsonify({
                "success": False,
                "message": "La catégorie n'existe pas",
                "code": 404
            }, 404)
        else:
            db.session.delete(category)
            db.session.commit()
            return jsonify({
                "success": True,
                "message": f"Catégorie {category.name} supprimée avec succès",
                "code": 200
            }, 200)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)


# get subcategories of a category
@mycat_bp.route('/<int:id>/subcategory', methods=['GET'])
@token_required
def getSubcategories(current_user, id: int):
    try:
        subcategories = SubCategory.query.filter_by(category=id).all()
        if subcategories is None:
            return jsonify({
                "success": False,
                "message": "Aucune sous-catégorie trouvée",
                "code": 404
            }, 404)
        else:
            subcategories = [subcategory.format() for subcategory in subcategories]
            return jsonify({
                "success": True,
                "subcategories": subcategories,
                "code": 200
            }, 200)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)

@mycat_bp.route('/<int:id>/subcategory', methods=['POST'])
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

#

# get products of a category
@mycat_bp.route('/<int:id>/product', methods=['GET'])
@token_required
def getProducts(current_user, id: int):
    try:
        products = Product.query.filter_by(category_id=id).all()
        if products is None:
            return jsonify({
                "success": False,
                "message": "Aucun produit trouvé",
                "code": 404
            }, 404)
        else:
            products = [product.format() for product in products]
            return jsonify({
                "success": True,
                "products": products,
                "code": 200
            }, 200)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)

@mycat_bp.route('/product', methods=['GET'])
def get_all_products():
    products = [product.format() for product in Product.query.all()]
    return jsonify({
        "success": True,
        "result": products
    })


@mycat_bp.route('/deliv', methods=['GET'])
def get_all():
    delivers = [deliv.format() for deliv in Deliver.query.all()]
    return jsonify({
        "success": True,
        "result": delivers
    })


@mycat_bp.route('/deliv', methods=['POST'])
@token_required
def create_deliv(current_user):
    try:
        body = request.get_json()
        name = body.get('Name', None)
        fname = body.get('FirstName', None)
        phone = body.get('Phone', None)
        password = body.get('Password', constants.DEFAULT_PASSWORD)
        quarter = body.get('Quarter', None)
        hire_date = body.get('HireDate', None)

        hire_date_obj = datetime.strptime(hire_date, '%Y-%m-%dT%H:%M:%S')
        hire_date = hire_date_obj.strftime('%Y-%m-%d')
        hire_date = datetime.strptime(hire_date, '%Y-%m-%d')

        # d = datetime.fromisoformat(hire_date[:-1]).astimezone(timezone.utc)
        # hire_date = d.strptime("%Y-%m-%d").date()
        # hire_date = datetime.strptime(hire_date, "%Y-%m-%d-%H:%M:%s").date()
        # TODO: check if the deliver already exists

        # hash password
        password = generate_password_hash(password)
        deliver = Deliver(name=name, firstname=fname, phone=phone, password=password, quarter=quarter,
                          hire_date=hire_date)
        if deliver is None:
            return jsonify({
                "success": False,
                "message": "Bad Request"
            }, 400)

        # check if deliver already exists
        if Deliver.check_if_exist(phone):
            return jsonify({
                "success": False,
                "message": "Deliver already exists"
            }, 400)
        else:
            deliver.insert()
            return jsonify({
                "success": True,
                "message": "Deliver created successfully"
            }, 201)
    except Exception as e:
        deliver_ = Deliver(name=name, firstname=fname, phone=phone, password=password, quarter=quarter, hire_date=hire_date)
        return jsonify({
            "success": False,
            "message": str(e) + "Bad Request"
        }, 400)
