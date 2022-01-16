from sqlalchemy import sql, Column, Sequence

from utils.db_api.database import db

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
