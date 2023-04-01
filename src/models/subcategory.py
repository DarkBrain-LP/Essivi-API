from src import db
from src.models.base_model import BaseModel


class SubCategory(db.Model, BaseModel):
    __tablename__ = "subcategory"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    category = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    is_active = db.Column(db.Boolean, nullable=True, default=True)
    # get the category_name from category table name
    category_name = db.relationship("Category", backref="subcategory", lazy=True)

    def __init__(self, name, category_id):
        self.name = name
        self.category = category_id

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "category_name": self.category_name.name
        }

    @classmethod
    def check_if_exist(cls, cat_id, name):
        return cls.query.filter_by(id=cat_id, name=name).first() is not None