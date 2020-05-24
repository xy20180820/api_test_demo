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
set_trace()
import allure
import pytest
@allure.feature('test_module_01')
@allure.story('test_story_01')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 0

@allure.feature('test_module_01')
@allure.story('test_story_02')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])