#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime
from core import engine, Base, create_all
from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, Unicode
from sqlalchemy import DateTime, Time
from sqlalchemy.orm import column_property


class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True, doc=u'用户id')
    username = column_property(firstname+ " " + lastname)
    email = Column(Unicode(128), unique=True, nullable=False, doc=u'邮箱')
    password = Column(String(128), nullable=False, doc=u'密码')
    firstname = Column(String(16), doc=u'用户姓')
    lastname = Column(String(16), doc=u'用户名')
    name = Column(String(32), doc=u'昵称')
    short_desc = Column(Unicode(256), doc=u'用户标语')
    birthday = Column(Time(), doc=u'出生日期')
    sex = Column(Boolean(), doc=u'性别, 1男2女', info=u'性别')
    qq = Column(String(16), doc=u'qq')
    telphone = Column(String(32), doc=u'联系方式，电话')
    is_admin = Column(Boolean, default=False, doc=u'是否为管理员')
    create_time = Column(Time(), default=datetime.now, doc=u'创建时间')

    def __init__(self, email, password, username=None):
        self.email = email
        self.password = password
        self.username = username

    def __repr__(self):
        return 'User:<uid: %s, username:%s, email: %s>' % (
            self.uid, self.username, self.email
        )

    @validates('email')
    def validate_email(self, key, email):
        pass


def drop_all():
    Base.metadata.drop_all()

if __name__ == '__main__':
    create_all()

