#!/user/bin/env python
# encoding: utf-8

from core import engine, Base, create_all
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, Boolean


class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return 'User:<uid: %s, username:%s, password: %s>' % (
            self.uid, self.username, self.password
        )

if __name__ == '__main__':
    create_all()

