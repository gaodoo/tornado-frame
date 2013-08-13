#!/usr/bin/env python
# encoding: utf-8

import re
import hashlib
from datetime import datetime
from core import engine, Base, create_all
from core import db_session
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer, String, Boolean, Unicode, Text
from sqlalchemy import DateTime, Time
from sqlalchemy.orm import column_property, validates
from sqlalchemy.orm import relationship, backref


class Useruser(Base):
    __tablename__ = 'user_user_attend'
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB',}

    uid = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    attend_uid = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    attend_time = Column(Time, default=datetime.now, doc=u'关注时间')

    def __repr__(self):
        return '<user: id: %s> attends <user: id: %s> at %s' % (
            self.uid, self.attend_uid, self.attend_time)

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB',}

    uid = Column(Integer, primary_key=True, doc=u'用户id')
    email = Column(Unicode(128), unique=True, nullable=False, doc=u'邮箱')
    password = Column(String(128), nullable=False, doc=u'密码')
    firstname = Column(String(16), doc=u'用户姓')
    lastname = Column(String(16), doc=u'用户名')
    username = column_property(firstname+ " " + lastname)
    name = Column(String(32), doc=u'昵称')
    short_desc = Column(Unicode(256), doc=u'用户标语')
    birthday = Column(Time(), doc=u'出生日期')
    sex = Column(Boolean(), doc=u'性别, 0男1女', info=u'性别')
    qq = Column(String(16), doc=u'qq')
    telphone = Column(String(32), doc=u'联系方式，电话')
    is_admin = Column(Boolean, default=False, doc=u'是否为管理员')
    create_time = Column(Time(), default=datetime.now, doc=u'创建时间')
    subjects = relationship('UserSubject', backref='sub_atteners', doc=u'关注话题')
    works = relationship('Work', backref="work_owner", doc=u"作品")
    sources = relationship('Source', backref="source_owner", doc=u"资源")
    articles = relationship('Article', backref='article_owner', doc=u'文章')
    questions = relationship('Question', backref='question_owner', doc=u'问题')
    answer = relationship('Answer', backref='anwser_owner', doc=u'回答')
    attends = relationship(
        'User',
        secondary='user_user_attend',
        primaryjoin=uid==Useruser.uid,
        secondaryjoin=uid==Useruser.attend_uid,
        backref='attenders'
    )

    def __init__(self, email, password, firstname=None, lastname=None):
        self.email = email
        self.password = hashlib.md5(password).digest()
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return 'User:<uid: %s, username:%s, email: %s>' % (
            self.uid, self.username, self.email
        )

    @validates('email')
    def validate_email(self, key, email):
        email_r = '\w+@\w+\.\w+'
        if re.match(email_r, email):
            return email
        else:
            raise ValueError("not correct email")

    @staticmethod
    def login(email, password, dbsession=db_session):
        """
        TODO: unittest
        return User instance or None
        """
        pw = hashlib.md5(password).digest()
        user = db_session.query(User).filter(User.email==email).filter(
            User.password==pw).first()
        return user

    @staticmethod
    def register(email, password, firstname, lastname, dbsession=db_session):
        """
        register new user
        TODO: 设计输出, try ..except
        """
        user = User(email, password)
        user.firstname = firstname
        user.lastname = lastname
        db_session.add(user).commit()
        return user


class UserSubject(Base):
    """
    用户-话题-关注表 model
    """
    __tablename__ = 'user_subject_relation'
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB',}
    uid = Column(Integer, ForeignKey('user.uid'), primary_key=True)
    sid = Column(Integer, ForeignKey('subject.sid'), primary_key=True)
    subject = relationship('Subject', backref='sub_attender')
    create_time = Column(Time(), default=datetime.now, doc=u'关注时间')


class Subject(Base):
    """
    话题表 models
    """
    __tablename__ = 'subject'
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB',}

    sid = Column(Integer, primary_key=True, doc=u'话题id')
    s_title = Column(Unicode(128), unique=True, nullable=False, doc="话题标题")
    s_desc = Column(Unicode(256), doc=u'标题简短描述')
    create_time = Column(Time(), default=datetime.now, doc=u'创建时间')

    def __init__(self, s_title, s_desc=None):
        self.s_title = s_title
        self.s_desc = s_desc


#class SourceBase(Base):
    #"""
    #抽象models, TODO: not tables
    #"""
    #__table_args__ = {'mysql_charset': 'utf8',
                      #'mysql_engine': 'InnoDB',}

    #create_time = Column(Time(), default=datetime.now, doc=u'创建时间')


class Work(Base):
    """
    作品主表
    """
    __tablename__ = 'work'
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB',}

    wid = Column(Integer, primary_key=True, doc=u'作品表')
    uid = Column(Integer, ForeignKey('user.uid'))
    w_title = Column(Unicode(128), nullable=False, doc=u'作品名')
    w_short_desc = Column(Unicode(256), doc=u'作品简述')
    w_long_desc = Column(Unicode(1024), doc=u'作品明细')
    w_type = Column(Integer, doc=u'作品类型') # TODO: 类型自动划分
    w_save_path = Column(String(512), doc=u'存储路径') # 二进制存储
    create_time = Column(Time(), default=datetime.now, doc=u'创建时间')

    def __init__(self, title, w_type, w_save_path, short_desc='', long_desc=''):
        self.w_title = title
        self.w_type = w_type
        self.w_save_path = w_save_path
        self.w_short_desc = short_desc
        self.w_long_desc = long_desc

class Source(Base):
    """
    资源主表
    """
    __tablename__ = 'source'
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB',}
    sc_id = Column(Integer, primary_key=True, doc=u'资源id')
    uid = Column(Integer, ForeignKey('user.uid'))
    sc_title = Column(Unicode(128), nullable=False, doc=u'资源名')
    sc_short_desc = Column(Unicode(256), doc=u'简述')
    sc_long_desc = Column(Unicode(1024), doc=u'明细')
    sc_type = Column(Integer, doc=u'资源类型')
    sc_save_path = Column(String(512), doc=u'存储路径')
    create_time = Column(Time(), default=datetime.now, doc=u'创建时间')

    def __init__(self, title, sc_type, sc_save_path, short_desc='', long_desc=''):
        self.sc_title = title
        self.sc_type = sc_type
        self.sc_save_path = sc_save_path
        self.sc_short_desc = short_desc
        self.sc_long_desc = long_desc


class Article(Base):
    """
    资源主表
    """
    __tablename__ = 'article'
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB',}

    at_id = Column(Integer, primary_key=True, doc=u'文章id')
    uid = Column(Integer, ForeignKey('user.uid'))
    at_title = Column(Unicode(128), nullable=False, doc=u'文章名')
    at_short_desc = Column(Unicode(256), doc=u'简述')
    at_long_desc = Column(Unicode(1024), doc=u'明细')
    content = Column(Text, doc=u'文章内容')
    create_time = Column(Time(), default=datetime.now, doc=u'创建时间')

    def __init__(self, title, at_type, at_save_path, short_desc='', long_desc=''):
        self.at_title = title
        self.at_type = at_type
        self.at_save_path = at_save_path
        self.at_short_desc = short_desc
        self.at_long_desc = long_desc


class Question(Base):
    """
    问题表
    """
    __tablename__ = 'question'
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB',}

    q_id = Column(Integer, primary_key=True, doc=u'问题id')
    uid = Column(Integer, ForeignKey('user.uid'))
    q_short_desc = Column(Unicode(256), doc=u'简述')
    q_long_desc = Column(Text, doc=u'明细')
    anwsers =  relationship('Answer', backref='question', doc=u'回答')
    create_time = Column(Time(), default=datetime.now, doc=u'创建时间')

    def __init__(self, short_desc, long_desc=''):
        self.q_short_desc = short_desc
        self.q_long_desc = q_long_desc


class Answer(Base):
    """
    问题回答表
    """
    __tablename__ = 'answer'
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB',}

    an_id = Column(Integer, primary_key=True, doc=u'回答id')
    q_id = Column(Integer, ForeignKey('question.q_id'))
    uid = Column(Integer, ForeignKey('user.uid'))
    an_content = Column(Text, doc=u'内容')
    create_time = Column(Time(), default=datetime.now, doc=u'创建时间')

    def __init__(self, content):
        self.an_content = content


def drop_all():
    Base.metadata.drop_all(engine)


__all__ = ['User', 'Useruser',]


if __name__ == '__main__':
    drop_all()
    create_all()
    print Base.metadata.tables
    print dir(Base.metadata)
