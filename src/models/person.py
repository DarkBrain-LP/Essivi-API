from src.extension import db


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    quarter = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(20), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "person",
        "polymorphic_on": type
    }

    def __init__(self, name, firstname, phone, password, quarter):
        self.name = name
        self.firstname = firstname
        self.phone = phone
        self.password = password
        self.quarter = quarter

    def format(self):
        return {
            "name": self.name,
            "firstname": self.firstname,
            "phone": self.phone,
            "quarter": self.quarter
        }

    # add to db
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

    # get by phone
    @classmethod
    def get_by_phone(cls, phone):
        return cls.query.filter_by(phone=phone).first()