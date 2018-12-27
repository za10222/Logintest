import unittest
import  HTMLTestRunner
import test_function
import test_security
import os

reportpath = 'result.html'
rs = open(reportpath, 'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=rs,title=u"登陆测试报告",description=u'课程测试作业')
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(test_function.Functiontest))
test_suite.addTest(unittest.makeSuite(test_security.Securitytest))
runner.run(test_suite)
rs.close()
os.system(os.getcwd()+'\\result.html')