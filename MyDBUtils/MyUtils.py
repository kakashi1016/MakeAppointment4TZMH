# -*- coding:utf-8 -*-
from MyRedisSession.RedisSession import SessionData

__author__ = 'Qian'

import uuid,base64,datetime

print r'cookie_secret:'
code = ''.join(['Hatake@', datetime.datetime.today().strftime('%Y-%m-%d'),'|cookie|',uuid.uuid1().__str__(),'|'])
print r'明文:'
print code
print r'Code:'
tmp = base64.b64encode(code)
print tmp
print r'解密'
print base64.b64decode(tmp)
print

print r'session_secret'
code = ''.join(['Hatake@', datetime.datetime.today().strftime('%Y-%m-%d'),'|session|',uuid.uuid1().__str__(),'|'])
print r'明文:'
print code
print r'Code:'
tmp = base64.b64encode(code)
print tmp
print r'解密'
print base64.b64decode(tmp)
print

print '-------'
print type(uuid.uuid1().hex)


session = SessionData('22ssss', 'ererere')
print session
print session.session_id


