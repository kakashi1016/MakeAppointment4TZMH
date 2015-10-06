# -*- coding:utf-8 -*-
__author__ = 'Qian'


import tornado.web
import tornado.gen
from tornado.httpclient import AsyncHTTPClient,HTTPRequest

import json
import urllib

class DemoHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        inArgs ={};
        inArgs['action']='dept'
        inArgs['CdateEX']='2015-09-22'
        inArgs['ampm']='2'
        inArgs['type']='2'
        myClient = AsyncHTTPClient()
        request = HTTPRequest('http://122.226.141.18:27016/wsgh/AjaxHelper.aspx',method='POST',
                              body=urllib.urlencode(inArgs))
                            #'action=dept&type=2&ampm=2&CdateEX=2015%2F9%2F20')


        response = yield  tornado.gen.Task(myClient.fetch, request)
        self.write(response.body)
        #print(json.dumps(response.body))
        self.finish()
        # print(response)
        # print()
        # print(json.load(response.body))
        #lst = ["python","www.itdiffer.com","qiwsir@gmail.com"]
        #self.render("Demo.html", info=lst)




