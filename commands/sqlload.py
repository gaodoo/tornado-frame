#!/usr/bin/env python
# encoding: utf-8

import sys
import cPickle as pickle
from os import path


def load_database(db_session, fixture):
    """
    load the database data for the fixtures,
    the fixture is a file path
    """
    # TODO: the fixture file path controls

    # load the fixture
    datas = pickle.loads(fixture)
    db_session.add_all(datas)
    db_session.commit()
    print "load database ok"

