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

# https://www.cnblogs.com/xswt/p/11549872.html
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import time
'''
# 1、请求超时，返回异常
import requests
url = 'http://www.google.com.hk'
r = requests.get(url)
print r.text
'''


'''
# 2、捕获超时时间；request请求默认的超时时间是21秒，实测大概是30秒
url = 'http://www.google.com.hk'
try:
    print time.strftime('%Y-%m-%d %H:%M:%S')
    r = requests.get(url)
except requests.exceptions.ConnectionError as e:
    print u'连接超时'
print time.strftime('%Y-%m-%d %H:%M:%S')

# 测试结果:2020-05-12 23:49:07 连接超时 2020-05-12 23:49:49
'''

'''
# 3、设置request请求超时时间
url = 'http://www.google.com.hk'
try:
    print time.strftime('%Y-%m-%d %H:%M:%S')
    r = requests.get(url, timeout=5)
except requests.exceptions.ConnectionError as e:
    print u'连接超时'
print time.strftime('%Y-%m-%d %H:%M:%S')
'''


# 4、request请求超时，设置重试次数
from requests.adapters import HTTPAdapter
# url = 'http://www.google.com.hk'
url = 'http://127.0.0.1:8888'
s = requests.Session()
s.mount("http://", HTTPAdapter(max_retries=3))
s.mount("https://", HTTPAdapter(max_retries=3))
try:
    print time.strftime('%Y-%m-%d %H:%M:%S')
    r = s.get(url, timeout=5)
except:
# except requests.exceptions.ConnectionError as e:
    print u'连接失败，该URL可能被墙掉了'
    # print e
print time.strftime('%Y-%m-%d %H:%M:%S')


