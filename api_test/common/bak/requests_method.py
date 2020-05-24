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
import requests
from nose.tools import set_trace
class Request_method(object):
    def __init__(self):
        pass

    def json_get_json(self,url,timeout = 5,**kwargs):
        '''

        :param url: 位置参数，必填
        :param timeout: 默认参数，非必填，默认为5
        :param kwargs:
        :return:
        '''
        set_trace()
        # url = kwargs.get('url')
        parmas = kwargs.get('params')
        headers = kwargs.get('headers')
        res = requests.get(url = url, timeout = timeout,params = params, headers = headers )
        return res

    def json_post_json(self):
        pass
