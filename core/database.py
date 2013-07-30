#!/user/bin/env python
# encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql://root:root@localhost/cgk', echo=True)
Base = declarative_base()

def create_all():
    Base.metadata.create_all()
