from src.extension import db
from src.models.person import Person


class Delivrer(Person):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, db.ForeignKey("personne.id"), primary_key=True)
    added_by = db.Column(db.Integer, db.ForeignKey("personne.id"), nullable=True)
    hire_date = db.Column(db.Date, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "delivrer"
    }
