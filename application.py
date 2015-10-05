# -*- coding:utf-8 -*-


__author__ = 'Qian'



import tornado.web
import os
from MyRedisSession.RedisSession import SessionManager

setting = dict(
  template_path=os.path.join(os.path.dirname(__file__), "MyTemplate"),
  static_path=os.path.join(os.path.dirname(__file__), "Static"),
  debug = True,
  cookie_secret = "SGF0YWtlQDIwMTUtMTAtMDV8Y29va2llfDkxNDY2NzdkLTZiMWQtMTFlNS04NTljLWE0NWU2MGQ3MzRmOXw=",
  session_secret = "SGF0YWtlQDIwMTUtMTAtMDV8c2Vzc2lvbnw5MTRiNzcyOC02YjFkLTExZTUtYjEwNC1hNDVlNjBkNzM0Zjl8",
  login_url = "/Login/",
  xsrf_cookies = True,
  session_timeout =600,

  )

#application = tornado.web.Application(
#  handlers=url,
#  **setting
#  )



class MyApplication(tornado.web.Application):
  def __init__(self, handlers, **settings):


    # 初始化父类 tornado.web.Application
    tornado.web.Application.__init__(self, handlers, **settings)
    # 初始化该类的 session_manager
    self.session_manager = SessionManager(settings["session_secret"], settings["session_timeout"])