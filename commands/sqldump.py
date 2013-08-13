#!/usr/bin/env python
# encoding: utf-8

import cPickle as pickle
from core import db_session
from core import db_session_test
from manager import Commands as Com


def dumps_database(test=False):
    # insert the project path
    project_dir = path.dirname(path.dirname(__file__))
    sys.path.insert(0, project_dir)

    import models

    # Warn: need the model define __all__ attri
    # and the Base and db_session need in the __all__
    results = []
    for model in models.__all__:
        if issubclass(model, models.Base):
            if not test:
                datas = db_session.query(
                    getattr(models, model)).all()
            else:
                datas = db_session_test.query(
                    getattr(models, model)).all()
            result.extends(datas)

    # dumps the data with pickle to file in the
    # the sys.args. if not dumps to the stdout
    file = sys.argv[1] or sys.stdout
    pickle.dump(result, file)
    print 'dumps database ok'


class Command(Com):

    def run(self, args, opts):
        pass

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        dumps_database(True)
    else:
        dumps_database()

