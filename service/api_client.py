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
import json
import requests
from nose.tools import set_trace
# set_trace()
s = requests.session()
url_login = "http://127.0.0.1:5000/login"
data = {'username': 'admin', 'password': 'admin'}
# r = requests.post(url=url_login, data=data)
r = s.post(url=url_login, data=data)
print r.status_code
print r.text
print r.headers
token = r.cookies['Authorization']  # 保存token，以后添加在请求的cookie中
headers = {
            'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
        }

cookies = {"Authorization": token}


# 1、post，添加data参数,cookies和headers上面都有，这里不就在重复定义了
# set_trace()
url = "http://127.0.0.1:5000/api/1.0/add_user"
# data = {'username': 'lily', 'passwd': 123456, 'age': 16, 'tel': '15899881000'}
data = {'username': 'lily', 'passwd': 123456, 'age': 16, 'tel': '15899881000'}

# r1 = requests.post(url=url, headers=headers, cookies=cookies, data=data)
r1 = s.post(url=url, headers=headers, cookies=cookies, data=data)
print r1.status_code
print r1.text
# print u'1.1、异常1，无参数'
r2 = s.post(url=url, headers=headers, cookies=cookies)
print r2.status_code
print r2.text
print u'1.2、异常2：无用户名或密码'
data = {'username': 'tom', 'age': 16, 'tel': '15899881000'}
r3 = s.post(url=url, headers=headers, cookies=cookies, data=data)
print r3.status_code
print r3.text

# 2、post，添加json参数,cookies和headers上面都有，这里不就在重复定义了
# set_trace()
url = "http://127.0.0.1:5000/api/1.0/add_user2"
# data = {'username': 'lily', 'passwd': 123456, 'age': 16, 'tel': '15899881000'}
data = {'username': 'lucy', 'passwd': 123123, 'age': 17, 'tel': '15899881001'}
data_json = json.dumps(data)  # 字典转换为json
# r1 = requests.post(url=url, headers=headers, cookies=cookies, json=data_json)
r1 = s.post(url=url, headers=headers, cookies=cookies, json=data_json)
print r1.status_code
print r1.text
# set_trace()
print '异常测试1：无参数'
r2 = s.post(url=url, headers=headers)
print r2.status_code
print r2.text
print '异常测试2：无密码'
data = {'username': 'lisi', 'age': 16, 'tel': '15899882000'}
data_json = json.dumps(data)
r3 = s.post(url=url, headers=headers,json=data_json)
print r3.status_code
print r3.text

# 3、get请求添加params
# set_trace()
url_get_user = "http://127.0.0.1:5000/api/1.0/get_user"
headers = {
            'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
        }
cookies = {"Authorization": token}
params = {"username": "admin"}  # 参数添加在url中的
# r1 = requests.get(url=url_get_user, headers=headers, cookies=cookies, params=params)
r1 = s.get(url=url_get_user, headers=headers, cookies=cookies, params=params)
print r1.status_code
print r1.text
print '3.1异常1：用户名为空'
r2 = s.get(url=url_get_user, headers=headers, cookies=cookies)
print r2.status_code
print r2.text
print '3.1异常1：用户名不存在'
params = {"username": "tom"}
r3 = s.get(url=url_get_user, headers=headers, cookies=cookies, params=params)
print r3.status_code
print r3.text

# 4、 get请求添加data参数
# set_trace()
url_get_user = "http://127.0.0.1:5000/api/1.0/get_user_data"
headers = {
            'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
        }
cookies = {"Authorization": token}

data = {"username": "admin"}  # 参数添加在url中的
# r1 = requests.get(url=url_get_user, headers=headers, cookies=cookies, data=data)
r1 = s.get(url=url_get_user, headers=headers, cookies=cookies, data=data)
print r1.status_code
print r1.text
# set_trace()
print '4.1异常1：用户名为空'
# data = {}
r2 = s.get(url=url_get_user, headers=headers, cookies=cookies)
print r2.status_code  # 有问题，返回400，应该返回401
print r2.text
print '4.2异常1：用户名不存在'
data = {"username": "tom"}
r3 = s.get(url=url_get_user, headers=headers, cookies=cookies, data=data)
print r3.status_code
print r3.text
# 5、post+json：删除用户
set_trace()
del_url = "http://127.0.0.1:5000/api/1.0/del_user"
# data = {'username': 'lily', 'passwd': 123456, 'age': 16, 'tel': '15899881000'}
data = {'username': 'lucy'}
data_json = json.dumps(data)  # 字典转换为json
# r1 = requests.post(url=url, headers=headers, cookies=cookies, json=data_json)
r1 = s.post(url=del_url, headers=headers, cookies=cookies, json=data_json)
print r1.status_code
print r1.text
print '5.1异常1：无参数'
r2 = s.post(url=del_url, headers=headers, cookies=cookies)
print r2.status_code
print r2.text

print '5.2异常1：无用户'
data = {'username': 'wangwu'}
data_json = json.dumps(data)
r3 = s.post(url=del_url, headers=headers, cookies=cookies, json=data_json)
print r3.status_code
print r3.text


# url_list = "http://127.0.0.1:5000/lists"
# # set_trace()
# headers = {
#             'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
#         }
# cookies = {"Authorization": token}
# r = requests.get(url=url_list, headers=headers, cookies=cookies)
# print r.status_code
# print r.text

# url_users = "http://127.0.0.1:5000/checkuser"
# headers = {
#             'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
#         }
# cookies = {"Authorization": token}
# # data = {"username": "admin"}
# r = requests.get(url=url_users, headers=headers, cookies=cookies)
# print r.status_code
# print r.text

# set_trace()
# url_get_users = "http://127.0.0.1:5000/getuser"
# headers = {
#             'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
#         }
# cookies = {"Authorization": token}
# data = {"username": "admin"}
# r = requests.get(url=url_get_users, headers=headers, cookies=cookies, data=data)
# print r.status_code
# print r.text
#
# # set_trace()
# url_get_users2 = "http://127.0.0.1:5000/getuser2"
# headers = {
#             'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
#         }
# cookies = {"Authorization": token}
# params = {"username": "admin"}  # 参数添加在url中的
# r = requests.get(url=url_get_users2, headers=headers, cookies=cookies, params=params)
# print r.status_code
# print r.text
#




