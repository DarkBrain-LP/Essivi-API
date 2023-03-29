# command class with db model inheritence
import datetime

from src import db
from src.models.base_model import BaseModel


class Command(db.Model, BaseModel):
    __tablename__ = "command"

    # add those fields' id, customer, deliverer, delivery_point, status, date
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    deliverer = db.Column(db.Integer, db.ForeignKey("deliver.id"), nullable=False)
    delivery_point = db.Column(db.Integer, db.ForeignKey("delivery_point.id"), nullable=False)
    status = db.Column(db.Integer, nullable=True, default=1)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, customer, deliverer, delivery_point):
        self.customer = customer
        self.deliverer = deliverer
        self.delivery_point = delivery_point
        self.status = 1
        self.date = datetime.datetime.now()

    def format(self):
        status = "encours"
        if self.status == -1:
            status = "annulé"
        elif self.status == 0:
            status = "livré"
        return {
            "customer": self.customer,
            "deliverer": self.deliverer,
            "deliveryPoint": self.delivery_point,
            "status": status,
            "date": self.date
        }
