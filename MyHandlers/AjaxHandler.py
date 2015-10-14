# -*- coding:utf-8 -*-
__author__ = 'Qian'

import urllib
import tornado
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
import json


class PatientInfoAjaxHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        inArgs ={};
        inArgs['action'] = 'patients'
        inArgs['cardno'] = self.get_argument('cardno', '')
        inArgs['name'] = self.get_argument('name', '').encode("utf-8")
        myClient = AsyncHTTPClient()
        request = HTTPRequest('http://122.226.141.18:27016/wsgh/AjaxHelper.aspx',method='POST',
                              body=urllib.urlencode(inArgs))

        response = yield  tornado.gen.Task(myClient.fetch, request)
        self.write(response.body)
        self.finish()

class DepartmentAjaxHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        inArgs ={};
        inArgs['action'] = 'dept'
        inArgs['ampm'] = self.get_argument('ampm', '')
        inArgs['CdateEX'] = self.get_argument('CdateEX', '')
        inArgs['type'] = self.get_argument('type', '')

        myClient = AsyncHTTPClient()
        request = HTTPRequest('http://122.226.141.18:27016/wsgh/AjaxHelper.aspx', method='POST',
                              body=urllib.urlencode(inArgs))

        response = yield  tornado.gen.Task(myClient.fetch, request)
        self.write(response.body)
        self.finish()

class DoctorAjaxHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        inArgs ={};
        inArgs['action'] = 'doc'
        inArgs['ampm'] = self.get_argument('ampm', '')
        inArgs['CdateEX'] = self.get_argument('CdateEX', '')
        inArgs['dept'] = self.get_argument('dept', '')

        myClient = AsyncHTTPClient()
        request = HTTPRequest('http://122.226.141.18:27016/wsgh/AjaxHelper.aspx',method='POST',
                              body=urllib.urlencode(inArgs))

        response = yield  tornado.gen.Task(myClient.fetch, request)
        self.write(response.body)
        self.finish()


class ClinicTimeAjaxHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        inArgs ={};
        inArgs['action'] = 'time'
        inArgs['ampm'] = self.get_argument('ampm', '')
        inArgs['CdateEX'] = self.get_argument('CdateEX', '')
        inArgs['groupid'] = self.get_argument('groupid', '')
        inArgs['doctor'] = self.get_argument('doctor', '')
        inArgs['dept'] = self.get_argument('dept', '')

        myClient = AsyncHTTPClient()
        request = HTTPRequest('http://122.226.141.18:27016/wsgh/AjaxHelper.aspx',method='POST',
                              body=urllib.urlencode(inArgs))

        response = yield  tornado.gen.Task(myClient.fetch, request)
        self.write(response.body)
        self.finish()


class DoctorPlanAjaxHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):

        url = 'http://122.226.141.18:28811/register/getplan/' +  self.get_argument('inW', '1') +'/'
        myClient = AsyncHTTPClient()

        response = yield  tornado.gen.Task(myClient.fetch, url)
        self.write(response.body)
        self.finish()





def Prepare4DEPT(ampm, date, type):
    inArgs ={};
    inArgs['action'] = 'dept'
    inArgs['ampm'] = ampm
    inArgs['CdateEX'] = date
    inArgs['type'] =type
    request = HTTPRequest('http://122.226.141.18:27016/wsgh/AjaxHelper.aspx',method='POST',
                          body=urllib.urlencode(inArgs))
    return request

