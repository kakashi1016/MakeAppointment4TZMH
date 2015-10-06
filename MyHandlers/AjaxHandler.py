# -*- coding:utf-8 -*-
__author__ = 'Qian'

import urllib
import tornado
from tornado.httpclient import AsyncHTTPClient, HTTPRequest



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
