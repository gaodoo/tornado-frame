#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


echo=False

engine = create_engine('mysql://root:root@localhost/cgk', echo=echo)
Base = declarative_base()

_Session = sessionmaker(bind=engine)
db_session = _Session(bind=engine)

# test db for unittest and ftstest

def create_all():
    Base.metadata.create_all(bind=engine)

def drop_all():
    Base.metadata.drop_all(bind=engine)
