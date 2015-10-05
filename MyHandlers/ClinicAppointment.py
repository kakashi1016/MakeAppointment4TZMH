# -*- coding:utf-8 -*-
__author__ = 'yq'
from MyHandlers.MyBaseHandler import MyBaseHandler

import tornado.gen
import datetime
class LoginHandler(MyBaseHandler):
    def get(self):
        today = datetime.date.today();
        self.render("01_login.html")

class ValidateHandler(MyBaseHandler):
    def get(self):
        today = datetime.date.today();
        self.render("02_validate.html")

class ChooseDroctorHandler(MyBaseHandler):
    @tornado.web.authenticated
    def get(self):
        today = datetime.date.today();
        self.render("03_chooseDroctor.html")

class TestHandler(MyBaseHandler):
    def get(self):
        self.session['token']='1'
        self.session.save();
        self.redirect("/")
