from src import Person, db


class Test(Person):
    __tablename__ = 'test'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    test_type = db.Column(db.String(30))

    __mapper_args__ = {
        "polymorphic_identity": "test"
    }

    def __init__(self, name, firstname, phone, password, quarter, type):
        super().__init__(name, firstname, phone, password, quarter)
        self.test_type = type