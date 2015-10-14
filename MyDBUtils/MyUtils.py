# -*- coding:utf-8 -*-
import base64

__author__ = 'Qian'

MyWeekDay4Chiness = {
    '0': r'周日',
    '1': r'周一',
    '2': r'周二',
    '3': r'周三',
    '4': r'周四',
    '5': r'周五',
    '6': r'周六',
}


# 加密,先base64,再拆分为3部分,127-首个,逆序拼接
def Encode4TZMH(inStr):

    inStr = base64.encodestring(inStr) # 对字符串编码
    inStr = bytearray(inStr, encoding="utf-8")
    length = len(inStr)
    text = [inStr[0:length/2], inStr[length/2:length/2+1], inStr[length/2+1:length]]
    tmp = "";
    for i in range(0,3,1):
        text[i][0] = 127 - text[i][0]
        tmp = ''.join([str(text[i]), tmp])
    return tmp

def Decode4TZMH(inStr):

    inStr = bytearray(inStr, encoding="utf-8")
    length = len(inStr)
    if (length %2 ==0):
        text = [inStr[0:length/2 -1], inStr[length/2 -1:length/2], inStr[length/2:length]]
    else:
        text = [inStr[0:length/2], inStr[length/2:length/2+1], inStr[length/2+1:length]]

    tmp = "";
    for i in range(0,3,1):
        text[i][0] = 127 - text[i][0]
        tmp = ''.join([str(text[i]), tmp])
    tmp = base64.decodestring(tmp) # 对字符串编码
    return tmp

