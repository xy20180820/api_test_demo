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
import configparser
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class Read_config(object):
    def __init__(self):
        # 获取配置文件的路径
        # set_trace()
        package_path = os.getcwd()
        conf_path = "\\config\\test_env.ini"
        # config_path = package_path + conf_path
        conf_path_name = package_path+conf_path
        # os.chdir(config_path)  # 切换到配置文件所在目录
        self.cf = configparser.ConfigParser()
        filename = self.cf.read(conf_path_name)

    def get_base_conf(self, opt):
        try:
            # set_trace()
            base_session = 'base'
            base_opt = self.cf.get(base_session,  opt)  # 获取指定session下的指定参数值
        except:
            base_opt = 'no opt'
        finally:
            return base_opt

    def get_request_conf(self, opt):
        try:
            # set_trace()
            request_session = 'request'
            request_opt = self.cf.get(request_session, opt) # 获取指定session下的指定参数值
        except:
            request_opt = 'no opt'
        finally:
            return request_opt

