from src.extension import db
from src.models.person import Person


class Customer(Person):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
    # added_by = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=True)
    delivery_points = db.relationship('DeliveryPoint', backref='customerEntity')

    __mapper_args__ = {
        "polymorphic_identity": "customer"
    }

    def __init__(self, name, firstname, phone, password, quarter, added_by):
        super().__init__(name, firstname, phone, password, quarter)
        self.added_by = added_by

    def format(self):
        return {
            "name": self.name,
            "firstname": self.firstname,
            "phone": self.phone,
            "quarter": self.quarter
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    # update and delete
    def update(self):
        db.session.commit()

    # delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()
