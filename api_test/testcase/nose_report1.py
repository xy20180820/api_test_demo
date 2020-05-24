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

import logging
# from test_case import new
from nose.tools import ok_
from nose.tools import eq_
import nose
import os
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
import sys

# TODO:jfjfjf
log = logging.getLogger(__name__)


def test_learn_1():
    u'''测试取消'''
    print 'xxx'
    log.info("afdffdfdfd")
    # raise SkipTest
    # print "test_lean_1"
    # pass
    # assert 1==2
    eq_(7, 9, msg=u"错误")


test_learn_1.slow = 1


@attr(mode=2)
def test_lean_2():
    u'''测试失败'''
    try:
        print "test_learn_2"
        ok_(4 == 3, msg="xxx")
        print sys._getframe().f_code.co_name
    except Exception:
        print sys._getframe().f_code.co_name


@attr(mode=2)
def test_lean_3():
    u'''测试成功'''
    pass


def setUp():
    # set_trace()
    global a
    print "0001 test setUp"
    # addCleanup(aa)


def tearDown():
    print "0001 test teardown"
    a = 'resource setup'
    b = 'c'
    # assert a==b
    print a