# -*- coding:utf-8 -*-
from MyRedisSession.RedisSession import SessionData

__author__ = 'Qian'

import uuid, base64, datetime

print r'cookie_secret:'
code = ''.join(['Hatake@', datetime.datetime.today().strftime('%Y-%m-%d'), '|cookie|', uuid.uuid1().__str__(), '|'])
print r'明文:'
print code
print r'Code:'
tmp = base64.b64encode(code)
print tmp
print r'解密'
print base64.b64decode(tmp)
print

print r'session_secret'
code = ''.join(['Hatake@', datetime.datetime.today().strftime('%Y-%m-%d'), '|session|', uuid.uuid1().__str__(), '|'])
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
    params = urllib.urlencode({'action': 'patients', 'cardno': 31683536, 'name': r'杨骞'})
    headers = {"Content-type": "application/x-www-form-urlencoded"
        , "Accept": "text/plain"}

    httpClient = httplib.HTTPConnection("122.226.141.18", 27016, timeout=30)
    httpClient.request("POST", "/wsgh/AjaxHelper.aspx", params, headers)

    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders()  # 获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()

from MyDBUtils.MyUtils import MyWeekDay4Chiness

date4Choose = [];
today = datetime.datetime.now()
if (today.hour >= 16):
    dStart = 2
else:
    dStart = 1

for i in range(dStart, dStart + 3):
    print i
    dTmp = today + datetime.timedelta(days=i)
    print dTmp
    tmp = dTmp.strftime("%Y-%m-%d")
    date4Choose.append({'id': 'date' + str(i - dStart), 'v': tmp,
                        's': ''.join([tmp, '(', MyWeekDay4Chiness[dTmp.weekday().__str__()], ')'])})

print date4Choose

import time

print int(time.strftime("%w"))
print type(int(time.strftime("%w")))

aaa = dict()
aaa['123']=34
print aaa







aaa0 = "Hatake@2015-10-14";
aaa = bytearray(aaa0, encoding="utf-8")
print len(aaa)
print type(aaa)

text= [aaa[0:len(aaa)/2],aaa[len(aaa)/2:len(aaa)/2+1],aaa[len(aaa)/2+1:len(aaa)]]


print text
tmp = [];
for i in range(0,3,1):
    text[i][0] = 255 - text[i][0]
    tmp.insert(2 -i, text[i])

print text
print tmp

import  MyUtils
aaaa = MyUtils.Encode4TZMH(aaa0)
print '=========original========='
print aaa0
print '=========encode========='
print aaaa
print '=========decode========='
aaaa = MyUtils.Decode4TZMH(aaaa)
print aaaa

print 5/2


