from src import db
from src.models.base_model import BaseModel


class Category(db.Model, BaseModel):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    is_active = db.Column(db.int, nullable=True, default=True)

    def __init__(self, name):
        self.name = name

    def format(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def check_if_exist(cls, name):
        return cls.query.filter_by(name=name).first() is not None

    @classmethod
    def check_if_id_exist(cls, id):
        return cls.query.filter_by(id=id).first() is not None

    # @classmethod
    # def check_if_subcat_exist(cls, name):
    #     return cls.query.fil