# from src import db
# from src.models.person import Person
#
#
# class Manager(Person):
#     __tablename__ = 'manager'
#     id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
#     hire_date = db.Column(db.Date, nullable=True)
#
#     __mapper_args__ = {
#         "polymorphic_identity": "manager"
#     }
#
#     def __init__(self, name, firstname, phone, password, quarter, hire_date):
#         super().__init__(name, firstname, phone, password, quarter)
#         self.hire_date = hire_date
#
#     def format(self):
#         return {
#             "name": self.name,
#             "firstname": self.firstname,
#             "phone": self.phone,
#             "quarter": self.quarter,
#             "hire_date": self.hire_date
#         }
#
#     # add to db
#     def insert(self):
#         db.session.add(self)
#         db.session.commit()
#
#     # update and delete
#     def update(self):
#         db.session.commit()
#
#     # delete
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#
#     # get all
#     @classmethod
#     def get_all(cls):
#         return cls.query.all()
#
#     # get by id
#     @classmethod
#     def get_by_id(cls, id):
#         return cls.query.filter_by(id=id).first()
#
#     # check if exist by phone number
#     @classmethod
#     def check_if_exist(cls, phone):
#         return cls.query.filter_by(phone=phone).first() is not None