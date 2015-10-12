# -*- coding:utf-8 -*-
__author__ = 'yq'
from MyHandlers.MyBaseHandler import MyBaseHandler
from MyDBUtils.MyUtils import MyWeekDay4Chiness
import tornado.gen
import datetime


class LoginHandler(MyBaseHandler):
    def get(self):
        self.render("01_login.html")

    def post(self):
        pMRN = self.get_argument('pMrn', '')
        pName = self.get_argument('pName', '')
        pAge = self.get_argument('pAge', '')
        pAgeUnit = self.get_argument('pAgeUnit_2', '')
        pGender = self.get_argument('pGender_2', '')
        pPCID = self.get_argument('pICID', '')
        pPhone = self.get_argument('pPhone', '')
        pAddress = self.get_argument('pAddress', '')

        self.session['token'] = '1'
        self.session['pMRN'] = pMRN
        self.session['pName'] = pName
        self.session['pAge'] = pAge
        self.session['pAgeUnit'] = pAgeUnit
        self.session['pGender'] = pGender
        self.session['pPCID'] = pPCID
        self.session['pPhone'] = pPhone
        self.session['pAddress'] = pAddress

        self.session.save();

        self.redirect("/ChooseDoctor/")


class ValidateHandler(MyBaseHandler):
    def get(self):
        today = datetime.date.today();
        self.render("02_validate.html")


class ChooseDroctorHandler(MyBaseHandler):
    # @tornado.web.authenticated
    def get(self):
        date4Choose = []
        today = datetime.datetime.now()
        if ( today.hour >= 16 ):
            dStart = 2
        else:
            dStart = 1
        for i in range(dStart, dStart + 3):
            dTmp = today + datetime.timedelta(days=i)
            tmp = dTmp.strftime("%Y-%m-%d")
            date4Choose.append({'id': 'date' + str(i-dStart), 'v': tmp,
                                's': ''.join([tmp, '(', MyWeekDay4Chiness[dTmp.strftime('%w')], ')'])})
        self.render("03_chooseDroctor.html", dList = date4Choose)


class TestHandler(MyBaseHandler):
    def get(self):
        self.session['token'] = '1'
        self.session.save()
        self.redirect("/")
