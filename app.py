#!/user/bin/env python
# encoding: utf-8

import tornado.web
import tornado.ioloop
import redis
from core import RedisSessionStore, Session
from core import engine
from settings import url_handlers, settings
from sqlalchemy.orm import scoped_session, sessionmaker


class Application(tornado.web.Application):
    def __init__(self, handlers, **settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        #self.db_session = db_session
        self.redis = redis.StrictRedis()
        self.session_store = RedisSessionStore(self.redis)
        #self.db = scoped_session(sessionmaker(bind=engine))
        self.db = sessionmaker(bind=engine)


application = Application(url_handlers, **settings)


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

