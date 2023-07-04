# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define, options
from app.urls import urls
from app.configs import configs

# Define the port on which the service starts
define("port", type=int, default=8080)

class CustomerApplication(tornado.web.Application):
    def __init__(self):
        handlers = urls
        settings = configs
        super(CustomerApplication, self).__init__(handlers=handlers, **settings)


def create_server():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomerApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()