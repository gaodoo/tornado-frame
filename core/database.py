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
engine_test = create_engine('mysql://root:root@localhost/cgk_test', echo=echo)
_Session_test = sessionmaker(bind=engine_test)
db_session_test = _Session(bind=engine_test)

def create_all():
    Base.metadata.create_all(bind=engine)

def create_all_for_test():
    Base.metadata.create_all(bind=engine_test)

def drop_all_for_test():
    Base.metadata.drop_all(bind=engine_test)
