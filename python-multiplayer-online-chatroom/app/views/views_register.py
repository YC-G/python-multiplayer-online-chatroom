# -*- coding: utf-8 -*-
import tornado.web

class RegisterHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h1>Register Page</h1>")