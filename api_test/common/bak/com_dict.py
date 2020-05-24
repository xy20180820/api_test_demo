# -------------------------------------------------------------------------------
# _*_encoding:utf-8_*_
# Name:        $[ActiveDoc-Name]
# Purpose:     
#
# Author:      $[UserName]
#
# Created:     $[DateTime-'DD/MM/YYYY'-DateFormat]
# Copyright:   (c) $[UserName] $[DateTime-'YYYY'-DateFormat]
# Licence:     <your licence>
# -------------------------------------------------------------------------------
# !/usr/bin/env python
# conding=utf-8
expect_json = {u'args': {u'email': u'a_kui@163.com', u'name': u'akui'}}
res_json={
u'origin': u'119.123.133.136, 119.123.133.136',
u'headers': {u'Host': u'httpbin.org', u'Accept-Encoding': u'gzip, deflate', u'Accept': u'*/*', u'User-Agent': u'python-requests/2.21.0'},
u'args': {u'email': u'a_kui@163.com', u'name': u'akui'},
u'url': u'https://httpbin.org/get?name=akui&email=a_kui%40163.com'}

def cmp_dict(dict1,dict2):
    for key in dict1:
        print key
        if key in dict2.keys():
            print dict1[key]
            print dict2[key]
            if dict1[key]==dict2[key]:
                print dict1[key],'yes'
            else:
                print '111',dict2[key]
        else:
            print '222',key
if __name__=='__main__':
    cmp_dict(expect_json,res_json)


