#!/usr/bin/env python
# encoding: utf-8

import sys
import cPickle as pickle
from os import path


def dumps_database():
    # insert the project path
    project_dir = path.dirname(path.dirname(__file__))
    sys.path.insert(0, project_dir)

    import models

    # Warn: need the model define __all__ attri
    # and the Base and db_session need in the __all__
    results = []
    for model in models.__all__:
        if issubclass(model, models.Base):
            datas = models.db_session.query(
                getattr(models, model)).all()
            result.extends(datas)

    # dumps the data with pickle to file in the
    # the sys.args. if not dumps to the stdout
    file = sys.argv[1] or sys.stdout
    pickle.dump(result, file)
    print 'dumps database ok'


