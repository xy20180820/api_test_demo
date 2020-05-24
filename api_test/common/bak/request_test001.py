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
import pdb
import requests
url = "http://httpbin.org/get?"
params = {"name": "lucy", "email": r"lucy@163.com"}
res = requests.get(url=url, params=params)
pdb.set_trace()
print res.status_code
print res.json()
res_result = res.json()
expect_result = {u'args': {u'email': u'lucy@163.com', u'name': u'lucy'}}
'''
(Pdb) res.json()['args']
{u'email': u'lucy@163.com', u'name': u'lucy'}

{u'origin': u'113.87.128.78, 113.87.128.78',
 u'headers': {u'Host': u'httpbin.org', 
 u'Accept-Encoding': u'gzip, deflate', 
 u'Accept': u'*/*', u'User-Agent': u'python-requests/2.21.0'}, 
 u'args': {u'email': u'lucy@163.com', u'name': u'lucy'}, 
 u'url': u'https://httpbin.org/get?name=lucy&email=lucy%40163.com'}

'''

