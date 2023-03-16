from src import db


class BaseModel:
    @classmethod
    def insert(cls, instance):
        db.session.add(instance)
        db.session.commit()

    # update and delete
    @classmethod
    def update(cls):
        db.session.commit()

    # delete
    @classmethod
    def delete(cls, instance):
        db.session.delete(instance)
        db.session.commit()