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
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from nose.tools import set_trace
from nose.tools import assert_equal
import json
set_trace()
a = {'a': 'aa'}
b = {'b': 'bb'}
assert_equal(a, b, msg=u'a:%s;b:%s' % (json.dumps(a), json.dumps(b)))


