#!/usr/bin/env python
# encoding: utf-8

import sys
import cPickle as pickle
from core import db_session
from manager import Commands as Com


def dump_database(f=sys.stdout):
    # insert the project path
    project_dir = path.dirname(path.dirname(__file__))
    sys.path.insert(0, project_dir)

    import models

    # Warn: need the model define __all__ attri
    # and the Base and db_session need in the __all__
    results = []
    for model in models.__all__:
        if issubclass(model, models.Base):
            datas = db_session.query(
                getattr(models, model)).all()
            result.extends(datas)

    # dumps the data to the file
    pickle.dump(result, f)
    print 'dumps database ok'


if __name__ == '__main__':
    try:
        if len(sys.argv) >1 :
            f = open(sys.argv[1])
        else:
            f = sys.stdout
    except Exception:
        print "open file: %s, errors" % f.name
    dumps_database(f)

