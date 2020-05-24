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
from nose.tools import set_trace
# set_trace()
import requests
from requests.adapters import HTTPAdapter
import json
from bs4 import BeautifulSoup
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
import logging
# set_trace()
logger = logging.getLogger(__name__)
up_path = os.getcwd()
# 导入Read_config，读取配置文件
package_path = up_path+'\\common\\'
sys.path.append(package_path)
from common.read_env_config_ok import Read_config
class Request_method(object):
    def __init__(self):
        # set_trace()
        # logger.info(u'创建Request实例对象')
        # 从配置文件中读取请求超时时间和重试次数
        get_request_config = Read_config()
        self.config_request_timeout = get_request_config.get_request_conf('request_timeout')
        config_request_retry = get_request_config.get_request_conf('request_retry')
        if self.config_request_timeout == 'no opt':
            self.config_request_timeout = 5
        if config_request_retry == 'no opt':
            config_request_retry = 3
        self.s = requests.session()
        self.s.mount("http://", HTTPAdapter(max_retries=config_request_retry))  # 增加请求超时重试次数
        self.s.mount("http://", HTTPAdapter(max_retries=config_request_retry))
        self.headers = {
            'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
        }
    #test_api_case中的测试用例调用此方法，判断request请求使用哪个方法，再调用Request_method对的对应方法

    def get_request_medthod(self, datas):
        '''
        :param datas:
        :return:res_code,res_result
        '''
        # set_trace()
        request_name = str(datas['method'])  #将unicode转换为字符串；request_name = request_get(表中method的值），调用下面的方法
        # print '调用的request的方法是:%s'%request_name
        # logger.info(u'调用的request的方法是:%s' %request_name)
        if hasattr(Request_method(), request_name):  # 如果Request_method类中，有request_name方法
            request_method = getattr(Request_method(), request_name)  # 则将该方法（函数）赋值给request_method
            res_code, res_result = request_method(datas)  # request_method调用实际的方法
            return res_code, res_result
        else:
            # print "datas['method']:%s填写错误" % datas['method']
            logger.info(u'request_method中无调用%s方法' % datas['method'])

    def request_get(self, datas):
        base_url = datas['base_url']
        api_command = datas['api_command']
        url = base_url+api_command
        params = datas['params']
        if params != '':
            params = eval(datas['params'])
            print 'ok'
        else:
            params = ''
            print 'nothing'
        # 优化：base_url放在配置项里：环境差异时，url就不一致，去别的环境调试时，避免必须修改代码
        # 此时读取配置文件，如果配置文件中，如果没有base_url配置项，或者为空，则使用base_url = datas['base_url']，否则有限使用配置的值
        # set_trace()
        res = requests.get(url=url, params=params)
        res_code = res.status_code
        # 字典
        res_result = res.json()
        return res_code, res_result
    def request_post(self,datas):
        # set_trace()
        base_url = datas['base_url']
        api_command = datas['api_command']
        url = base_url+api_command
        data = datas['params']
        if data != '':
            data = eval(datas['params'])
            print 'ok'
        else:
            data = ''
            print 'nothing'
        # set_trace()
        res = requests.post(url=url, data=data)
        res_code = res.status_code
        res_result = res.json()
        return res_code, res_result

    # 编写一个独立的登录函数，给下面需要登录才可调用的接口使用
    def login_post_data(self):
        try:
            s = requests.session()
            url_login = "http://127.0.0.1:5000/login"
            data = {'username': 'admin', 'password': 'admin'}
            r = s.post(url=url_login, data=data)
            token = r.cookies['Authorization']  # 保存token，以后添加在请求的cookie中
            headers = {
                'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
            }

            cookies = {"Authorization": token}
            return cookies
        except:
            logger.info("如果存在错误，已记录在日志文件中")
            logger.exception(sys.exc_info())  # 将错误信息记录在日志文件中


    def request_post_cookies_data(self, datas):
        try:
            # set_trace()
            # # 因为调用这些接口需要先登录，所以，这里增加登录，返回cookies；此处可以优化：将登录独立成一个函数 已使用login_post_data代替
            # s = requests.session()
            # url_login = "http://127.0.0.1:5000/login"
            # data = {'username': 'admin', 'password': 'admin'}
            # r = s.post(url=url_login, data=data)
            # token = r.cookies['Authorization']  # 保存token，以后添加在请求的cookie中
            # headers = {
            #     'ua': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
            # }
            #
            # cookies = {"Authorization": token}
            logger.info(u'调用request_post_cookies_data')
            s = self.s
            cookies = self.login_post_data()  # 调用登录函数，获取cookies
            headers = eval(datas['headers'])  # 将unicode转换字典
            # 1、post，添加data参数,cookies和headers上面都有，这里不就在重复定义了
            # set_trace()
            base_url = datas['base_url']  # 读取url
            api_command = datas['api_command']  # 读取接口名称
            url = base_url + api_command  # 将url和接口名称拼接成request请求的完整地址
            # set_trace()

            data = datas['params']  # 读取请求参数
            if data != '':
                data = eval(datas['params'])  # 将unicode的data转换为dict类型的data
                # 增加了请求超时时间
                res = s.post(url=url, headers=headers, cookies=cookies, data=data, timeout=5)  # 发送请求
            else:
                res = s.post(url=url, headers=headers, cookies=cookies, timeout=5)  # 异常测试，无data时，发送此请求（无data）
            res_code = res.status_code  # 状态码的类型是int
            res_result = res.json()  # 返回字典结果
            logger.info(u'res_code:%s;'
                        u'res_result:%s' % (res_code, res_result))
            return res_code, res_result
        # except requests.exceptions.ConnectionError as e:
        #     logger.error(u'request请求超时，已经重试了3次')
        #     logger.error(u'错误信息为：%s' %e)

        except:
            logger.info(u"如果存在错误，已记录在日志文件中")
            logger.exception(sys.exc_info())  # 将错误信息记录在日志文件中(包括请求超时的异常10061）
    def request_post_cookies_data_del_user(self,datas):
        pass

    def request_post_cookies_json(self, datas):
        try:
            # set_trace()
            logger.info(u'调用request_post_cookies_json')
            s = self.s
            cookies = self.login_post_data()
            headers = eval(datas['headers'])  # 将unicode转换字典

            # 1、post，添加data参数,cookies和headers上面都有，这里不就在重复定义了
            # set_trace()
            # url2 = "http://127.0.0.1:5000/api/1.0/add_user"
            base_url = datas['base_url']
            api_command = datas['api_command']
            url = base_url + api_command

            data = datas['params']
            if data != '':
                data = eval(datas['params'])  # 将unicode转换为字典
                data = json.dumps(data)  # 将字典转换为json
                res = s.post(url=url, headers=headers, cookies=cookies, json=data)
            else:
                res = s.post(url=url, headers=headers, cookies=cookies)
            print res.status_code
            print res.json
            print res.text
            res_code = res.status_code
            res_result = res.json()  # 返回json
            # res_result = res.text  # 返回字符串
            logger.info(u'request_post_cookies_json返回res_code，res_result')
            return res_code, res_result
        except:
            logger.info("如果存在错误，已记录在日志文件中")
            logger.exception(sys.exc_info())  # 将错误信息记录在日志文件中


    def request_post_cookies_json_del_user(self):
        pass
    def request_get_params(self, datas):
        try:
            logger.info(u'调用request_get_params')
            s = self.s
            cookies = self.login_post_data()
            headers = eval(datas['headers'])  # 将unicode转换字典

            # set_trace()
            base_url = datas['base_url']
            api_command = datas['api_command']
            url = base_url + api_command
            data = datas['params']
            if data != '':
                data = eval(data)  # 字符串转换为字典
                res = s.get(url=url, headers=headers, cookies=cookies, params=data)
            else:
                res = s.get(url=url, headers=headers, cookies=cookies)
            res_code = res.status_code
            res_result = res.json()
            # set_trace()
            logger.info(u'request_get_params返回res_code，res_result')
            return res_code, res_result
        except:
            logger.info("如果存在错误，已记录在日志文件中")
            logger.exception(sys.exc_info())  # 将错误信息记录在日志文件中


    def request_get_data(self, datas):
        try:
            logger.info(u'调用request_get_data')
            s = self.s
            cookies = self.login_post_data()  # 调用登录函数，获取cookies
            headers = eval(datas['headers'])  # 将unicode转换字典
            # set_trace()
            base_url = datas['base_url']
            api_command = datas['api_command']
            url = base_url + api_command
            data = datas['params']
            if data != '':
                print 'ok'
                data = eval(data)  # 字符串转换为字典
                # url_get_user = "http://127.0.0.1:5000/api/1.0/get_user_data"
                # data = {"username": "admin"}
                res = s.get(url=url, headers=headers, cookies=cookies, data=data)
            else:
                print 'nothing'
                data = ''
                res = s.get(url=url, headers=headers, cookies=cookies)
            print res.status_code
            print res.json
            print res.text
            res_code = res.status_code
            res_result = res.json()
            # set_trace()
            logger.info(u'request_get_data返回res_code，res_result')
            return res_code, res_result
        except:
            logger.info("如果存在错误，已记录在日志文件中")
            logger.exception(sys.exc_info())  # 将错误信息记录在日志文件中



    def request_post_session(self, datas):
        # set_trace()
        session = requests.session()
        result = session.get("http://127.0.0.1:5000/login")
        soup = BeautifulSoup(result.text, "html.parser")
        inputs = soup.find_all("input", id="csrf_token")
        csrf_token = inputs[0].attrs["value"]
        data = {"csrf_token": csrf_token, "email": "xu123@126.com", "password": "xu@123"}
        result = session.post("http://127.0.0.1:5000/login", data=data)
        if "Logged in successfully" in result.text:
            print '14:ok'
        else:
            print '14:error'
        cookies = result.cookies
        cookies_input = {}
        cookies_input[cookies.items()[0][0]] = cookies.items()[0][1]

        base_url = datas['base_url']
        api_command = datas['api_command']
        url = base_url + api_command
        data = datas['params']
        if data != '':
            data = eval(datas['params'])
            print 'ok'
        else:
            data = ''
            print 'nothing'
        # set_trace()
        data["csrf_token"] = csrf_token
        headers = datas['headers']
        headers = eval(headers)# unicode专业为字典https://www.cnblogs.com/OnlyDreams/p/7850920.html

        #-------------------
        # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0","Accept": '"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"',}
        # data = {"csrf_token": csrf_token, "nickname": "xu123", "about_me": "20190911502:xu123"}

        # -----------------
        set_trace()
        res = session.post(url=url, data=data, headers=headers, cookies=cookies_input)
        res_code = res.status_code
        if "Your changes have been saved" in res.text:
            res_result = "Your changes have been saved"
        else:
            print 'error'
        return res_code, res_result





