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
'''
1、调试测试用例
(venv_http_api_test) D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_d
emo01>nosetests -v -s testcase\nose_test.py:Test_001
执行时，会将nose_test.py中所有类的顶层语句执行：x =1 print。。。会被执行；
同时class Test_002中的y =1 pring。。。也会被执行
2、跑用例：
(venv_http_api_test) D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01>
nosetests -v -s testcase\test_api_case.py
3、生成报告：
先安装pip install nose-html-reporting
nosetests -v -s -a report demo07\BaiduTest6.py --with-html --html-report=demo07\report\demo7-002report.html
nosetests  -v -s  testcase\test_api_case.py --with-html --html-report=\report\report001.html

4、生成更漂亮的报告：https://www.cnblogs.com/landhu/p/7126039.html
a、安装pip install nose-allure-plugin
allure generate report\result8 -o \report\result8_html_report
此处报告的路径要写绝对路径，否则报告会保存到D:\report\result9_html_report
(virtualenv-test) D:\python2.7.13\mypython\selenium2\06-selenium2-cahpter8-page-object\demo11>allure generate report\result9 -o D:\python2.7.13\mypython\selenium2\06-selenium2-cahpte
r8-page-object\demo11\report\result9_html_report
allure generate report\result10 -o D:\python2.7.13\mypython\selenium2\06-selenium2-cahpter8-page-object\demo11\report\result10_html_report
先生成html报告：
(venv_http_api_test) D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01>nosetests  -v -s  testcase\test_api_
case.py --with-html --html-report=\report\report001\report001.html

b、生成xml报告：
安装pip install nose-allure-plugin
(venv_http_api_test) D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01
nosetests -v testcase\test_api_case.py --with-allure --logdir=D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01\report\result0032 --logging-config=config\logging.conf
c、将xml报告转换为html：

(venv_http_api_test) D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01
allure generate report\result0031 -o D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01\report\report0031
问题：生成的html报告数据为空，
原因：要开启服务才可以查看，命令如下：allure report open
https://blog.csdn.net/chenfei_5201213/article/details/80982929
解决方法1：使用pycharm→浏览器打开（firefox存在问题，都是loading，无法加载数据）
解决方法2：https://www.cnblogs.com/ivywoon/p/11990946.html
使用Microsoft Edge浏览器打开即可
5、生成日志：
nosetests -v testcase\test_api_case.py --logging-config=D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01\config\logging.conf

日志：
a、配置日志文件：test_demo01\config\logging.conf，该配置默认输出到控制台和指定文件；日志级别为：都为debug
b、代码实现：日志可显示中文
import logging
logger = logging.getLogger(__name__)  创建日志器

logger.debug(u'')
logger.info(u'Test_api001--step2:create request object')
logging.warning(u'warning')
logger.error(u'')
如何需要在子程序实现日志，方法相同，且日志会保存到同一个文件中
c、执行命令：添加日志配置文件
D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01>nosetests -v testcase\test_api_case.py --logging-config=config\logging.conf

6、日志2：nose-printlog
nosetests -v testcase\test_api_case.py --with-allure --logdir=D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01\report\result0036 --with-printlog
allure generate report\result0036 -o D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01\report\report0036


7、日志到报告中
https://www.jianshu.com/p/bd2eba80f8d5
https://www.cnblogs.com/zzgblg/p/10039029.html

8、
https://testerhome.com/topics/5738

'''
# ddt说明：https://blog.csdn.net/sinat_41774836/article/details/85061007
from nose.tools import set_trace
import sys
import os
import allure
from nose.plugins.attrib import attr
import nose
# set_trace()
# package_path = os.getcwd()
package_path = os.path.dirname(os.getcwd())
sys.path.append(package_path)
import requests
import json
import ddt
import inspect
from nose.tools import assert_equal
from nose.tools import assert_equals
from nose.tools import assert_dict_contains_subset
from nose.tools import assert_in

from nose.tools import assert_dict_equal
from nose.plugins.skip import SkipTest
import logging
logger = logging.getLogger(__name__)  # 日志中：日志器名称为模块名，每个模块运行时显示各自的模块名称

# set_trace()
#test_demo01加入了sys.path，就可以通过下面的方式导入一个类,此时会执行被导入类的import部分
from common.open_execl_xlrd_ok import Open_excel
#导入request请求的类
from request.request_method import Request_method
# set_trace()
# 具体Environment参数可自行设置
allure.environment(app_package='com.mobile.fm')
allure.environment(app_activity='com.mobile.fm.activity')
allure.environment(device_name='aad464')
allure.environment(platform_name='Android')
p1 = sys.getdefaultencoding()
import sys
reload(sys)
sys.setdefaultencoding('utf8')
p2 = sys.getdefaultencoding()
print p1
print p2
'''
问题：
w10系统，cmd运行下面代码
set_trace()
logger.info(u'Test_api006接口开始测试...')
报错：Failure: IOError ([Errno 0] Error) ... ERROR
解决方法：
方法1：在代码中添加下面代码
import sys
reload(sys)
sys.setdefaultencoding('utf8')
补充：大部分情况方法1可以解决，解决不了时，使用此方法：在logger.info(u'Test_api006接口开始测试...')之后使用settrace，不要在它前面使用settrace
方法2：不要在logger.info包含中文的前面加断点set_trace()
方法3：logger.info打印信息不要包含中文
    
'''
# set_trace()
# 使用Sheet1
# @allure.step(u'jskjfdk')
# @allure.feature(u'接口1：')
# @ddt.ddt
# class Test_api001(object):
#     # set_trace()
#     logger.info(u'步骤1：Test_api001--step1:--read Sheet1')
#     # set_trace()
#     ex = Open_excel('Sheet1')  # 传入参数：sheet表的名称
#     test_data = ex.open_excel() # 返回sheet表的所有数据，test_data格式为列表，列表每个元素为字典（表头为键值，每一个的数据为value）
#     # 将excel的每一行作为列表的一个元素，组成列表test_data1
#     # def setUp(self):
#     #     print("Start!")
#     # def tearDown(self):
#     #     print("end!")
#     # set_trace()
#     @classmethod
#     def setUpClass(cls):
#         # set_trace()
#         logger.info(u'Test_api001--step2:create request object')
#         cls.call_request = Request_method()
#         print u'setUpClass......'
#     @classmethod
#     def tearDownClass(cls):
#         # set_trace()
#         print u'tearDownClass......'
#     def setUp(self):
#         # set_trace()
#         print u'setup...'
#     def tearDown(self):
#         # set_trace()
#         print u'teardown...'
#     # @ddt.data(*self.test_data)
#     # @allure.story(u'接口1→场景1')
#     @allure.severity('critical')
#     @ddt.data(*test_data)  # 使用ddt，使sheet表每一行都数据执行下面的函数
#     def test_api001(self, datas):
#         # set_trace()
#         """
#         用例描述：get方法，每条用例的描述
#         :param datas:
#         :return:
#         """
#         # #近一步优化，将request请求进行封装
#         # base_url = datas['base_url']
#         # api_command = datas['api_command']
#         # url = base_url+api_command
#         # # unicode 转换为str
#         # # 当params为空的unicode时，使用eval会报错，所以，需要判断一下：
#         # # 当params为非空时，使用eval(datas['params'])将unicode转换为str
#         # # 当params为空的nnicode类型时，重新定义params='',此时params为空的str类型；
#         # params = datas['params']
#         # if params != '':
#         #     params = eval(datas['params'])
#         #     print 'ok'
#         # else:
#         #     params = ''
#         #     print 'nothing'
#         # # set_trace()
#         # res = requests.get(url=url, params=params)
#         # res_code = res.status_code
#         # # 字典
#         # res_result = res.json()
#
#         # set_trace()
#         # u'调用request方法3：需要cls.call_request = Request_method()，如果此方法不太灵活，可以继续使用“调用request方法1”，需屏蔽此行'
#         # u'cls.call_request = Request_method()创建实例→调用get_request_medthod方法→判断datas['method']'
#         # u'的值，如果该值是Request_method的一个方法→调用该方法（该方法也在Request_method类里）'
#         logger.info(u'步骤3：Test_api001--step3:execute case：api001')
#         # logger.info(u'接口名称%s：；测试用例：%s') %(self.__class__.__name__, sys._getframe().f_code.co_name)
#         # 调用request_method.py中的request方法，发送请求
#         res_code, res_result = self.call_request.get_request_medthod(datas)
#
#
#         # 调用request方法2：
#         # # 调用reques方法，返回状态码和请求结果,使用此方法，可以把cls.call_request = Request_method()屏蔽掉
#         # request_name = str(datas['method'])
#         # if hasattr(Request_method(),request_name):
#         #     request_method = getattr(Request_method(),request_name)
#         #     res_code, res_result = request_method(datas)
#         # else:
#         #     print "datas['method']:%s填写错误"%datas['method']
#
#         # 调用request方法1：直接调用Request_method类的request方法（可能会导致写了很多request方法）
#         # res_code,res_result = self.call_request.request_get(datas)#使用此行，需要在setUpClass(cls)中添加cls.call_request = Request_method()
#         # #将此方式优化，如果datas['method']在Request_method()类中，就调用该方法，要求：此接口使用哪种request请求，则datas['method']的值必须填写Request_method类中对应的方法名
#         set_trace()
#         expect_code = int(datas['expect_code'])
#         # excel中读取的expect_result是unicode格式，使用eval转换dict
#         expect_result = eval(datas['expect_result'])
#         # 比较状态码和结果
#         assert_equal(expect_code, res_code,msg=u'请求错误%d' %res_code)
#         assert_dict_contains_subset(expect_result, res_result, msg=u'预期结果错误%s'%res_result)
# Test_api002的用例跳过，不执行
class Test_api002(object):
    @classmethod
    def setUpClass(cls):
        logger.info(u'Test_api002:类开始...')
    @classmethod
    def tearDownClass(cls):
        logger.info(u'Test_api002:类结束...')
    def setUp(self):
        logger.info(u'用例开始...')
    def tearDwon(self):
        logger.info(u'用例结束...')

    def test_api002(self):
        logger.info(u'跳过用例：test_api002')
        raise SkipTest
# Test_api003的用例执行失败
class Test_api003(object):
    try:
        @classmethod
        def setUpClass(cls):
            logger.info(u'Test_api003:类开始...')
        @classmethod
        def tearDownClass(cls):
            logger.info(u'Test_api003:类结束...')
        def setUp(self):
            logger.info(u'用例开始...')
        def tearDwon(self):
            logger.info(u'用例结束...')

        def test_api003(self):
            # set_trace()
            logger.info(u'失败用例：test_api003')
            assert_equal(1, 2, msg=u'1 !=2')  # 用例执行失败，错误信息会记录xml和html报告中
        # print(1 / 0)  # 为了触发错误，跳转到expec处，捕获异常，记录日志
    except:  # 捕获所有异常，并且记录在日志文件中（非用例执行失败的代码错误）
        set_trace()
        logger.info("如果存在错误，已记录在日志文件中")
        logger.exception(sys.exc_info())  # 将错误信息记录在日志文件中
# # 使用Sheet4
# @ddt.ddt
# class Test_api004(object):
#     # set_trace()
#     ex = Open_excel('Sheet4')
#     test_data = ex.open_excel()
#     @classmethod
#     def setUpClass(cls):
#         # set_trace()
#         cls.call_request = Request_method()
#         print u'setUpClass......'
#     @classmethod
#     def tearDownClass(cls):
#         # set_trace()
#         print u'tearDownClass......'
#     def setUp(self):
#         # set_trace()
#         print u'setup...'
#     def tearDown(self):
#         # set_trace()
#         print u'teardown...'
#     # @ddt.data(*self.test_data)
#     @allure.severity('critical')
#     @ddt.data(*test_data)
#     # u'执行此行时，需要已经读取了excel表中的数据，所以 下面2行代码必须放在类顶层执行，'
#     # u'在 setUpClass  中执行会报错：NameError: name 'test_data' is not defined'
#     # ex = Open_excel('Sheet4')
#     # test_data = ex.open_excel()
#     def test_api004(self, datas):
#         """
#         用例描述：post方法，每条用例的描述
#         :param datas:
#         :return:
#         """
#         # set_trace()
#         res_code, res_result = self.call_request.get_request_medthod(datas)
#         expect_code = int(datas['expect_code'])
#         # excel中读取的expect_result是unicode格式，使用eval转换dict
#         expect_result = eval(datas['expect_result'])
#         # 比较状态码和结果
#         assert_equal(expect_code, res_code, msg=u'请求错误%d'%res_code)
#         assert_dict_contains_subset(expect_result, res_result, msg=u'预期结果错误%s'%res_result)

# Test_api005-009，服务器返回的都是json格式的数据
# data001.xlsx中sheet6的用例用于测试Test_api006接口
@ddt.ddt
class Test_api005(object):
    try:
        # set_trace()
        logger.info(u'Test_api005接口读取Sheet5数据...')
        # logger.info(u'Test_api005 start...')
        ex = Open_excel('Sheet5')  # 创建实例，Open_excel用于操作execl，打开execl
        test_data = ex.open_excel()  # 将指定sheet表中的数据读取出来，每一行数据组成列表test_data的一个元素
        @classmethod
        def setUpClass(cls):
            # cls.name == cls.__class__.__name__
            # print cls.name
            print 'setUpClass......'
            logger.info(u'Test_api005接口测试开始...')
            # set_trace()
            cls.call_request = Request_method()  # 这个类执行之前的准备工作：创建实例，使用类的属性call_request调用Request_method中的request请求方法

        @classmethod
        def tearDownClass(cls):   # 这个类执行之后的清理工作
            # set_trace()

            print 'tearDownClass......'
            logger.info(u'Test_api005接口测试结束...')

        def setUp(self):
            # set_trace()
            print 'setup...'  # 每个函数执行之前的准备工作
        def tearDown(self):
            # set_trace()
            print 'teardown...'  # 每个函数执行之后的清理工作
        @allure.severity('critical')
        @ddt.data(*test_data)  # datas的每一行数据，调用一次test_api005方法
        def test_api005(self, datas):
            """
            用例描述：post方法，每条用例的描述
            :param datas:
            :return:
            """
            # set_trace()
            logger.info(u'Test_api005接口---test_api005用例开始...')
            # logger.info('Test_api005接口用例%s开始测试...' % inspect.stack()[1][3])
            # logger.info('Test_api005接口用例%s开始测试...' % sys._getframe().f_code.co_name)

            res_code, res_result = self.call_request.get_request_medthod(datas)  # 调用request请求方法，获取返回状态码和返回结果
            expect_code = int(datas['expect_code'])  # datas['expect_code']的类型是浮点数，将其转换为int
            # excel中读取的expect_result是unicode格式，使用eval转换dict
            # expect_result = eval(datas['expect_result'])
            expect_result = datas['expect_result']  # 这是一个unicode的字符串
            expect_result = json.loads(expect_result)  # 将预期结果转换为字典
            # res_result = json.loads(res_result)  # 转换为字典
            # 比较状态码和结果
            # set_trace()
            assert_equal(expect_code, res_code, msg='expect_code:%d;res_code:%d' % (expect_code, res_code))
            assert_equal(expect_result, res_result, msg='expect_result:%s;res_result:%s' % (json.dumps(expect_result), json.dumps(res_result)))
    except:  # 捕获所有异常，并且记录在日志文件中（非用例执行失败的代码错误）
        # set_trace()
        logger.error(u"Test_api005如果存在错误，已记录在日志文件中")
        logger.exception(sys.exc_info())
# data001.xlsx中sheet6的用例用于测试Test_api006接口
@ddt.ddt
class Test_api006(object):
    try:
        # set_trace()
        logger.info(u'Test_api006接口读取Sheet6数据...')
        ex = Open_excel('Sheet6')
        test_data = ex.open_excel()
        @classmethod
        def setUpClass(cls):
            # set_trace()
            logger.info(u'Test_api006接口测试开始...')
            cls.call_request = Request_method()
            print 'setUpClass......'
        @classmethod
        def tearDownClass(cls):
            # set_trace()
            print 'tearDownClass......'
            logger.info(u'Test_api006接口测试结束...')
        def setUp(self):
            # set_trace()
            print 'setup...'

        def tearDown(self):
            # set_trace()
            print 'teardown...'
        # @ddt.data(*self.test_data)
        @allure.severity('critical')
        @ddt.data(*test_data)
        # u'执行此行时，需要已经读取了excel表中的数据，所以 下面2行代码必须放在类顶层执行，'
        # u'在 setUpClass  中执行会报错：NameError: name 'test_data' is not defined'
        # ex = Open_excel('Sheet4')
        # test_data = ex.open_excel()
        def test_api006(self, datas):
            """
            用例描述：post方法，每条用例的描述
            :param datas:
            :return:
            """
            # set_trace()
            logger.info(u'Test_api006接口用例test_api006开始测试...')
            res_code, res_result = self.call_request.get_request_medthod(datas)
            expect_code = int(datas['expect_code'])
            # excel中读取的expect_result是unicode格式，使用eval转换dict
            # expect_result = eval(datas['expect_result'])
            expect_result = datas['expect_result']
            expect_result = json.loads(expect_result)  # 转换为字典
            # res_result = json.loads(res_result)  # 转换为字典
            # 比较状态码和结果
            assert_equal(expect_code, res_code, msg='expect_code:%d;res_code:%d' % (expect_code, res_code))
            assert_equal(expect_result, res_result, msg='expect_result:%s;res_result:%s' % (json.dumps(expect_result), json.dumps(res_result)))
    except:  # 捕获所有异常，并且记录在日志文件中（非用例执行失败的代码错误）
        # set_trace()
        logger.error(u"Test_api006如果存在错误，已记录在日志文件中")
        logger.exception(sys.exc_info())

# data001.xlsx中sheet7的用例用于测试Test_api007接口
@ddt.ddt
class Test_api007(object):
    try:
        # set_trace()
        logger.info(u'Test_api007接口读取Sheet7数据...')
        ex = Open_excel('Sheet8')
        test_data = ex.open_excel()

        @classmethod
        def setUpClass(cls):
            # set_trace()
            logger.info(u'Test_api007接口测试结束...')
            cls.call_request = Request_method()
            print 'setUpClass......'

        @classmethod
        def tearDownClass(cls):
            # set_trace()
            print 'tearDownClass......'

        def setUp(self):
            # set_trace()
            print 'setup...'

        def tearDown(self):
            # set_trace()
            print 'teardown...'

        # @ddt.data(*self.test_data)
        @allure.severity('critical')
        @ddt.data(*test_data)
        # u'执行此行时，需要已经读取了excel表中的数据，所以 下面2行代码必须放在类顶层执行，'
        # u'在 setUpClass  中执行会报错：NameError: name 'test_data' is not defined'
        # ex = Open_excel('Sheet4')
        # test_data = ex.open_excel()
        def test_api007(self, datas):
            """
            用例描述：post方法，每条用例的描述
            :param datas:
            :return:
            """
            # set_trace()
            logger.info(u'Test_api007接口用例test_api007开始测试...')
            res_code, res_result = self.call_request.get_request_medthod(datas)
            expect_code = int(datas['expect_code'])
            # excel中读取的expect_result是unicode格式，使用eval转换dict
            # expect_result = eval(datas['expect_result'])
            expect_result = datas['expect_result']
            expect_result = json.loads(expect_result)  # 转换为字典
            # res_result = json.loads(res_result)  # 转换为字典
            # 比较状态码和结果

            assert_equal(expect_code, res_code, msg='expect_code:%d;res_code:%d' % (expect_code, res_code))
            assert_equal(expect_result, res_result,msg='expect_result:%s;res_result:%s' % (json.dumps(expect_result), json.dumps(res_result)))
    except:  # 捕获所有异常，并且记录在日志文件中（非用例执行失败的代码错误）
        # set_trace()
        logger.error(u"Test_api007如果存在错误，已记录在日志文件中")
        logger.exception(sys.exc_info())
# data001.xlsx中sheet9的用例用于测试Test_api009接口
@ddt.ddt
class Test_api008(object):
    try:
        # set_trace()
        logger.info(u'Test_api008接口读取Sheet8数据...')
        ex = Open_excel('Sheet8')
        test_data = ex.open_excel()

        @classmethod
        def setUpClass(cls):
            # set_trace()
            logger.info(u'Test_api008接口测试开始...')
            cls.call_request = Request_method()
            print 'setUpClass......'

        @classmethod
        def tearDownClass(cls):
            # set_trace()
            print 'tearDownClass......'
            logger.info(u'Test_api008接口测试结束...')

        def setUp(self):
            # set_trace()
            print 'setup...'

        def tearDown(self):
            # set_trace()
            print 'teardown...'

        # @ddt.data(*self.test_data)
        @allure.severity('critical')
        @ddt.data(*test_data)
        # u'执行此行时，需要已经读取了excel表中的数据，所以 下面2行代码必须放在类顶层执行，'
        # u'在 setUpClass  中执行会报错：NameError: name 'test_data' is not defined'
        # ex = Open_excel('Sheet4')
        # test_data = ex.open_excel()
        def test_api008(self, datas):
            """
            用例描述：post方法，每条用例的描述
            :param datas:
            :return:
            """
            # set_trace()
            logger.info(u'Test_api008接口用例test_api008开始测试...')
            res_code, res_result = self.call_request.get_request_medthod(datas)
            expect_code = int(datas['expect_code'])
            # excel中读取的expect_result是unicode格式，使用eval转换dict
            # expect_result = eval(datas['expect_result'])
            expect_result = datas['expect_result']
            expect_result = json.loads(expect_result)  # 转换为字典
            # res_result = json.loads(res_result)  # 转换为字典
            # 比较状态码和结果
            # set_trace()
            assert_equal(expect_code, res_code, msg='expect_code:%d;res_code:%d' % (expect_code, res_code))
            assert_equal(expect_result, res_result,
                         msg='expect_result:%s;res_result:%s' % (json.dumps(expect_result), json.dumps(res_result)))
    except:  # 捕获所有异常，并且记录在日志文件中（非用例执行失败的代码错误）
        # set_trace()
        logger.info(u"Test_api008如果存在错误，已记录在日志文件中")
        logger.exception(sys.exc_info())
# data001.xlsx中sheet10的用例用于测试Test_api0010接口
@ddt.ddt
class Test_api009(object):
    try:
        # set_trace()
        logger.info(u'Test_api009接口读取Sheet9数据...')
        ex = Open_excel('Sheet9')
        test_data = ex.open_excel()

        @classmethod
        def setUpClass(cls):
            # set_trace()
            logger.info(u'Test_api009接口测试开始...')
            cls.call_request = Request_method()
            print 'setUpClass......'

        @classmethod
        def tearDownClass(cls):
            # set_trace()
            print 'tearDownClass......'
            logger.info(u'Test_api009接口测试结束...')

        def setUp(self):
            # set_trace()
            print 'setup...'

        def tearDown(self):
            # set_trace()
            print 'teardown...'

        # @ddt.data(*self.test_data)
        @allure.severity('critical')
        @ddt.data(*test_data)
        # u'执行此行时，需要已经读取了excel表中的数据，所以 下面2行代码必须放在类顶层执行，'
        # u'在 setUpClass  中执行会报错：NameError: name 'test_data' is not defined'
        # ex = Open_excel('Sheet4')
        # test_data = ex.open_excel()
        def test_api009(self, datas):
            """
            用例描述：post方法，每条用例的描述
            :param datas:
            :return:
            """
            # set_trace()
            logger.info(u'Test_api009接口用例test_api009开始测试...')
            res_code, res_result = self.call_request.get_request_medthod(datas)
            expect_code = int(datas['expect_code'])
            # excel中读取的expect_result是unicode格式，使用eval转换dict
            # expect_result = eval(datas['expect_result'])
            expect_result = datas['expect_result']
            expect_result = json.loads(expect_result)  # 转换为字典
            # res_result = json.loads(res_result)  # 转换为字典
            # 比较状态码和结果
            assert_equal(expect_code, res_code, msg='expect_code:%d;res_code:%d' % (expect_code, res_code))
            assert_equal(expect_result, res_result, msg='expect_result:%s;res_result:%s' % (json.dumps(expect_result), json.dumps(res_result)))
    except:  # 捕获所有异常，并且记录在日志文件中（非用例执行失败的代码错误）
        # set_trace()
        logger.info(u"Test_api009如果存在错误，已记录在日志文件中")
        logger.exception(sys.exc_info())

'''
1、
D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo00>
nosetests -v -a debug testcase\test_case01.py
2、日志

'''

