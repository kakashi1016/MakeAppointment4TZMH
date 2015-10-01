# -*- coding:utf-8 -*-
__author__ = 'yq'

import tornado.web
import tornado.gen
import datetime
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        today = datetime.date.today();
        self.render("01_login.html")

class ValidateHandler(tornado.web.RequestHandler):
    def get(self):
        today = datetime.date.today();
        self.render("02_validate.html")

class ChooseDroctorHandler(tornado.web.RequestHandler):
    def get(self):
        today = datetime.date.today();
        self.render("03_chooseDroctor.html")
