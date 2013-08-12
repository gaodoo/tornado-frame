#!/usr/bin/env python
# encoding: utf-8

import tornado.web
import tornado.ioloop
import redis
from core import RedisSessionStore
from core import db_session
from core import engine
from settings import url_handlers, settings
from sqlalchemy.orm import scoped_session, sessionmaker


class Application(tornado.web.Application):
    def __init__(self, handlers, db_session, **settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        #self.db_session = db_session
        self.redis = redis.StrictRedis()
        self.session_store = RedisSessionStore(self.redis)
        #self.db = scoped_session(sessionmaker(bind=engine))
        self.db = db_session


application = Application(url_handlers, db_session, **settings)


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

