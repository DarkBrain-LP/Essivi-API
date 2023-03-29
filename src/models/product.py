from src import db
from src.models.base_model import BaseModel


# product class
class Product(db.Model, BaseModel):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    volume_litter = db.Column(db.Float, nullable=True)
    price = db.Column(db.Float, nullable=False)
    number = db.Column(db.Integer, nullable=True)
    category = db.Column(db.Integer, db.ForeignKey("subcategory.id"), nullable=False)

    @classmethod
    def check_if_exist(cls, name):
        return cls.query.filter_by(name=name).first() is not None

    @classmethod
    def check_if_id_exist(cls, id):
        return cls.query.filter_by(id=id).first() is not None