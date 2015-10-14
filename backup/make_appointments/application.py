# -*- coding:utf-8 -*-
__author__ = 'Qian'

from url import url

import tornado.web
import os

setting = dict(
  template_path=os.path.join(os.path.dirname(__file__),"MyTemplate"),
  static_path=os.path.join(os.path.dirname(__file__),"Static"),
  debug = True,
  )

application = tornado.web.Application(
  handlers=url,
  **setting
  )