from src import db
from src.models.base_model import BaseModel


class DeliveryPoint(db.Model, BaseModel):
    __tablename__ = "delivery_point"

    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    customer = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    point_name = db.Column(db.String, nullable=False)

    def __init__(self, longitude, latitude, point_name, customer):
        self.longitude = longitude
        self.latitude = latitude
        self.point_name = point_name
        self.customer = customer

    def format(self):
        return {
            "name": self.point_name,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "customer": self.customer
        }
