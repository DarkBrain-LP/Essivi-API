from flask import Blueprint, request, jsonify
from pvlib import location

from src import  db
from src.models.customer import Customer
from src.models.deliver import Deliver
from src.models.delivery_point import DeliveryPoint
from src.models.person import Person
from src.utils import constants
from src.utils.wrapper import token_required

customer_bp = Blueprint("customer_bp", __name__, url_prefix='/customer')


@token_required
@customer_bp.route('/', methods=['POST'])
def create_customer(current_user):
    auth = request.authorization
    current_user_phone = current_user.phone
    # if current_user.phone == current_user_phone:
    #     print('cool')
    # try catch
    try:
        body = request.get_json()
        name = body.get('name', None)
        fname = body.get('firstname', None)
        phone = body.get('phone', None)
        password = body.get('password', constants.DEFAULT_PASSWORD)
        quarter = body.get('quarter', None)
        location = body.get('location', None)

        if Deliver.check_if_exist(current_user_phone):
            added_by_ = Person.get_by_phone(current_user_phone).id

        customer = Customer(name=name, firstname=fname, phone=phone, password=password, quarter=quarter,
                            added_by=added_by_)

        # TODO: check if the customer already exists

        # TODO: add the location

        if Person.check_exists(phone):
            return jsonify({
                "success": False,
                "message": "Une personne existe déjà avec ce numéro"
            }, 400)
        else:
            db.session.add(customer)
            db.session.commit()
            # customer.insert()
            return jsonify({
                "success": True,
                "message": "Client ajouté avec succès"
            }, 201)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Une erreur s'est produite"
        }, 400)


@customer_bp.route('<int:id>/deliveryPoint/', methods=['POST'])
@token_required
def add_delivery_point(customer_id: int, current_user):
    if Customer.check_exists_by_id(id=customer_id):
        return jsonify({
            "success": False,
            "message": "Le client n'existe pas"
        }, 400)
    else:
        body = request.get_json()
        longitude = float(body.get('longitude', None))
        latitude = float(body.get('latitude', None))
        name = body.get('name', constants.DEFAULT_DELIVERY_POINT_NAME)

        deli_point = DeliveryPoint(longitude=longitude, latitude=latitude, point_name=name, customer=customer_id)

        # customer delivery points
        customer = Customer.get_by_id(customer_id)
        if customer.id == current_user.id:
            print('cool')
        deli_points = customer.delivery_points

        if any([(dp.longitude == longitude and dp.latitude == latitude) or dp.name == name  for dp in deli_points]):
            return jsonify({
                "success": False,
                "message": "coordonnées ou nom de lieu déjà existant pour ce client"
            }, 400)
        else:
            db.session.add(deli_points)
            customer.delivery_points.append(deli_point)
            db.session.commit()
            # customer.update()
            return jsonify({
                "success": True,
                "point": deli_point.format(),
                "totalPoints": len(customer.delivery_points),
                "message": "Point ajouté avec succès"
            }, 400)