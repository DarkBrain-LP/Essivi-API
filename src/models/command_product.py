# this a flask class that manage the many to many relationship between product and command
from src import db
from src.models.base_model import BaseModel


class CommandProduct(db.Model, BaseModel):
    __tablename__ = "command_product"
    # add those fields' id, command, product, quantity
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.Integer, db.ForeignKey("command.id"), nullable=False)
    product = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, command, product, quantity):
        self.command = command
        self.product = product
        self.quantity = quantity

    def format(self):
        # return the json based format of the object
        return {
            "command": self.command,
            "product": self.product,
            "quantity": self.quantity
        }
