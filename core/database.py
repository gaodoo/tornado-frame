#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('mysql://root:root@localhost/cgk', echo=True)
engine_test = create_engine('mysql://root:root@localhost/test', echo=True)
Base = declarative_base()
_Session = sessionmaker(bind=engine)
session = _Session(bind=engine)


def create_all():
    Base.metadata.create_all(bind=engine)

def create_all_for_test():
    Base.metadata.create_all(bind=engine_test)

