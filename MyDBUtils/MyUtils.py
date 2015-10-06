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





import httplib, urllib

httpClient = None
try:
    params = urllib.urlencode({'action': 'patients', 'cardno': 31683536, 'name':r'杨骞'})
    headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/plain"}

    httpClient = httplib.HTTPConnection("122.226.141.18", 27016, timeout=30)
    httpClient.request("POST", "/wsgh/AjaxHelper.aspx", params, headers)

    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()


