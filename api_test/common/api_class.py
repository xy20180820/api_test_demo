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

class Test_get_ip_info(object):
    def __init__(self):
        self.url = "http://httpbin.org/"

    def test_get_ip_info(self):
        res = get_json()
        res_status_code = res.status_code
        res_resutl = res.json()["origin"]
        return res_status_code,res_resutl
