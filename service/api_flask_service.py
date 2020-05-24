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

# https://www.jianshu.com/p/7bff6e3d869b
import json
import os
from flask import Flask, g, jsonify, make_response, session
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import Flask,session, redirect, url_for, render_template, request
from nose.tools import set_trace
import functools
app = Flask(__name__)
# app.config['SECRET_KEY'] = os.urandom(24)
app.config['SECRET_KEY'] = 'secret key here'
serializer = Serializer(app.config['SECRET_KEY'], expires_in=1800)
app.config['JSON_AS_ASCII'] = False  # jsonify支持中文
auth = HTTPTokenAuth(scheme='Bearer')
# users = ['John', 'Susan']
# usr_list = {
#     'admin': 'admin',
#     'John': '123456',
#     'Susan': '123'}
usr_list = {
    'admin': {'passwd': 'admin', 'tel': '15899870001', 'age': 18},
}
users = usr_list.keys()
users_token = {}
for u in users:
    users_token[u] = ''



def genrate_token(user):
    from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
    secret_key = 'secret key here'
    # user = 'John'
    serializer = Serializer(secret_key=secret_key, expires_in=1800)
    token = serializer.dumps({'username': user})
    users_token[user] = token
    return token


@app.route('/')
def index():
    return render_template('login_test12_token6.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # set_trace()
        log_n = request.form['username']
        log_p = request.form['password']
        if log_n in usr_list.keys():  # 判断用户名是否在usr_list中，判断用户合法性
            if log_p == usr_list[log_n]['passwd']:  # 判断该提交的用户名密码是否正确
                token = genrate_token(log_n)  # 通过用户名生成token
                resp = make_response(render_template('test12_token6_lists.html'))  # 登录成功后需要返回一个网页
                resp.set_cookie('Authorization', token)  # 返回网页将token值保存到cookie中
                session['username'] = log_n  # 添加session
                print token
                return resp
# 某些接口需要登录才可访问，编写一个登录验证的装饰器，增加在接口前即可使用
# https://www.jianshu.com/p/7bff6e3d869b
def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
        secret_key = 'secret key here'
        serializer = Serializer(secret_key=secret_key, expires_in=1800)
        try:
            # set_trace()
            # 在请求头上拿到token
            # token = request.headers["z-token"]
            token = request.cookies['Authorization']
            # my_session = request.cookies['session']  # 获取session,加密后的值
            s_name = session.get('username')  # 获取session,session={'username,'log_n'}
        except Exception:
            # 没接收的到token,给前端抛出错误
            # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
            return jsonify(code=4103, msg='缺少参数token')

        # s = serializer.loads(token)
        try:
            # set_trace()
            data = serializer.loads(token)
            s_name == data['username']  # 增加session认证


        except Exception:
            return jsonify(code=4101, msg="登录已过期")

        return view_func(*args, **kwargs)

    return verify_token
'''
接口0
1、接口说明：添加用户信息
URL：http://127.0.0.1:5000/lists
request参数：无
method：get

response：网页
例子：
'''

@app.route('/lists')
@login_required #必须登录的装饰器校验
def lists():
    # 需要认证请求头中cookies中保存的token
    # set_trace()
    # token = request.cookies['Authorization']
    # # token = request.headers['token']
    # verify_token(token)
    return 'lists ok!'
    # lists_ok = {'l1': 1, 'l2': 2, 'l3': 3}
    # return jsonify(d1=lists_ok, status_code=200, )


# 1、处理post请求的data参数
'''
接口文档规范：http://www.manongjc.com/detail/15-gdhfeymreilwqhe.html  （包含认证）
接口1
1、接口说明：添加用户信息
URL：http://127.0.0.1:5000/api/1.0/add_user
request参数：字典
data = {'username': 'lily', 'passwd': 123456, 'age': 16, 'tel': '15899881000'}
method：post

response：所有用户的信息，json格式
例子：
# data001.xlsx中sheet6的用例用于测试Test_api006接口
'''
@app.route('/api/1.0/add_user', methods=['POST', 'GET'])
@login_required
def add_user():
    # set_trace()
    try:
        if request.method == 'POST':
            r_data = request.form
            d_data = dict(r_data)
            if not bool(d_data):  # 判断字典是否为空
            # if d_data == None:
                data = {'msg': u'请求参数为空'}
                code = 401
            else:
                if 'username' not in d_data.keys() or 'passwd' not in d_data.keys():
                    data = {'msg': u'用户名或密码为空'}
                    code = 402
                else:
                    name = d_data['username'][0]  # d_data['username']竟然是个列表
                    # d1={}
                    # d1['passwd'] = d_data['passwd']
                    # d1['age'] = d_data['age']
                    # d1['tel'] = d_data['tel']
                    # usr_list[name] = d1
                    usr_list[name] = {'passwd':d_data['passwd'][0], 'age':d_data['age'][0], 'tel':d_data['tel'][0]}
                    data = usr_list
                    code = 200
    except:
        data = {'msg': u'请求方法错误'}
        return jsonify(data), 400
    finally:
        return jsonify(data=data, ), code
# 2、 处理post+json参数
'''
接口2
1、接口说明：添加用户信息
URL：http://127.0.0.1:5000/api/1.0/add_user
request参数：json
data = {'username': 'lucy', 'passwd': 123123, 'age': 17, 'tel': '15899881001'}
data_json = json.dumps(data)
method：post
response：所有用户的信息，json格式
例子：
# data001.xlsx中sheet7的用例用于测试Test_api007接口
'''
@app.route('/api/1.0/add_user2', methods=['POST', 'GET'])
@login_required
def add_user2():
    # set_trace()
    try:
        if request.method == 'POST':
            # r_data = request.form
            r_data = request.get_json()
            if r_data==None:
                data = {'msg': u'请求参数为空'}
                code = 401
            else:
                d_data = json.loads(r_data)  # json转换为字典
                if 'username' not in d_data.keys() or 'passwd' not in d_data.keys():
                    data = {'msg': u'用户名或密码为空'}
                    code = 402
                else:
                    usr_list[d_data['username']] = {'passwd': d_data['passwd'], 'age': d_data['age'], 'tel': d_data['tel']}
                    # name = r_data['username']
                    # usr_list[name] = {'passwd':r_data['passwd'], 'age':r_data['age'], 'tel':r_data['tel']}
                    # return jsonify(usr_list), 201,
                    data = usr_list
                    code = 200

    except:
        data = {'msg': u'请求方法错误'}
        code = 400
    # else:
    #     data = {'msg': u'请求方法错误'}
    #     return jsonify(data), 400
    finally:
        return jsonify(data=data, ), code

# 3、处理get请求的params参数

'''
接口3
1、接口说明：获取指定用户信息
URL：http://127.0.0.1:5000/api/1.0/get_user
request参数：字典
params = {"username": "admin"} 
method：post
response：所有用户的信息，json格式
例子
# data001.xlsx中sheet8的用例用于测试Test_api008接口
'''
@app.route('/api/1.0/get_user')
@login_required
def get_user():
    try:
        name = request.args.get('username')
        if name == None:
            data = {'msg': u'请求参数为空'}
            code = 401
        else:
            if name not in usr_list.keys():
                data = {'msg': u'用户名不存在'}
                code = 402
            else:
                r_data = usr_list[name]
                data = r_data
                code = 200
                # return jsonify(data), 200
    except:
        data = {'msg': u'请求方法错误'}
        code = 400
    finally:
        return jsonify(data=data, ), code




# data001.xlsx中sheet9的用例用于测试Test_api009接口
# 4、处理get请求的data参数
@app.route('/api/1.0/get_user_data')
@login_required
def get_user_data():
    # set_trace()
    try:
        r_data = request.values
        name = r_data.get('username')
        if name == None:
            data = {'msg': u'请求参数为空'}
            code = 401
        else:
            # name = r_data['username']
            if name not in usr_list.keys():
                data = {'msg': u'用户名不存在'}
                code = 402
            else:
                data = usr_list[name]
                code = 200
    except:
        data = {'msg': u'请求参数错误'}
        code = 400
    finally:
        return jsonify(data=data, ), code

    # name = request.form['username']
    # if name in usr_list.keys():
    #     data = usr_list[name]
    #     print type(data)
    #     return jsonify(data), 200
    # else:
    #     data = {'msg': u'用户名不存在'}
    #     return jsonify(data), 400
# 5、删除用户
'''
接口5
1、接口说明：删除指定用户信息
URL：http://127.0.0.1:5000/api/1.0/del_user
request参数:json
data = {"username": "admin"}
method：post
response：所有用户的信息，json格式
例子
# data001.xlsx中sheet10的用例用于测试Test_api0010接口
'''
@app.route('/api/1.0/del_user', methods=['POST', 'GET'])
@login_required
def del_user():
    # set_trace()
    try:
        if request.method == 'POST':
            r_data = request.get_json()

            if r_data == None:
                data = {'msg': u'请求参数为空'}
                code = 401
            else:
                d_data = json.loads(r_data)  # json转换为字典
                if d_data['username'] not in usr_list.keys():
                    data = {'msg': u'用户名不存在'}
                    code = 402
                else:
                    del usr_list[d_data['username']]
                    data = usr_list
                    code = 200
    except:
        data = {'msg': u'请求方法错误'}
        code = 400
    finally:
        return jsonify(data=data, ), code

@app.route('/api/1.0/getuser')
@login_required
def getuser():
    # set_trace()
    username = request.form['username']
    return username

@app.route('/api/1.0/getuser2')
@login_required
def getuser2():
    # set_trace()
    username = request.args.get("username")  # 接收get方法的request中的params参数
    # return username
    data = {'username': username, 'age': 19}
    return jsonify(data), 201
# 前后端json参数传递，https://blog.csdn.net/hanyuyang19940104/article/details/80519321


app.run(host="127.0.0.1", port=5000, debug=True)



'''
https://blog.csdn.net/weixin_34124577/article/details/92506110
https://blog.csdn.net/hwhsong/article/details/84959755
https://blog.csdn.net/u011181633/article/details/43229387/
'''