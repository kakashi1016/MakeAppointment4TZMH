# -*- coding:utf-8 -*-
__author__ = 'Qian'


import tornado.ioloop
import tornado.options
import tornado.httpserver
from application import MyApplication,setting
from url import url

from tornado.options import define,options
define("port",default=8000,help="run on th given port",type=int)

def main():
  tornado.options.parse_command_line()


  application = MyApplication(handlers=url, **setting )


  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(options.port)
  print 'Development server is running at http://127.0.0.1:%s/' % options.port
  print 'Quit the server with Control-C'
  tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
  main()