#!/usr/bin/env  python
#-*- coding:utf-8  -*-
def convertCookieStrToDict(cookieStr):
    StrArray = CookieStr.split(";")
    tempDict = {}
    for i in StrArray:
        iArray =i.split("=")
        tempDict[iArray[0]] = iArray[1]
        return tempDictk