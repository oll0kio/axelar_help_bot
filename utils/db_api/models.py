from sqlalchemy import sql, Column, Sequence

from utils.db_api.database import db


class Service(db.Model):
    __tablename__ = 'services'
    querry: sql.Select

    id = Column(db.Integer, Sequence("user_id_seq"), primary_key=True)
    category_code = Column(db.String(20))
    category_name = Column(db.String(50))

    name = Column(db.String(25))
    photo = Column(db.String(255))
    short_description = Column(db.String(50))
    description = Column(db.String(512))
    link = Column(db.String(255))

    def __repr__(self):
        return f"{self.name} \n{self.description}"


class User(db.Model):
    __tablename__ = 'users'
    querry: sql.Select

    id = Column(db.Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(db.BigInteger)
    full_name = Column(db.String(50))
    username = Column(db.String(50))
    referral = Column(db.Integer)

    def __repr__(self):
        return "<User(id='{}', fullname='{}', username='{}')>".format(
            self.id, self.full_name, self.username)
