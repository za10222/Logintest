# import os
import random
import  HTMLTestRunner
from selenium import webdriver
import requests
from time import sleep
import unittest

from selenium.webdriver.common.keys import Keys

def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str
class Securitytest(unittest.TestCase):
    def setUp(self):
        self.id1 = 'mercury'
        self.pw = 'mercury'
        chrome_options = webdriver.ChromeOptions()

        # chrome_options.set_headless()
        # chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(1)
        self.driver.set_page_load_timeout(10)
    def tearDown(self):
        self.driver.quit()


# 不登录的情况下，在浏览器中直接输入登录后的URL地址,验证是否会重新定向到用户登录界面
#     @unittest.skip('no')
    def test_case1(self):
        """不登录的情况下，在浏览器中直接输入登录后的URL地址,验证是否会重新定向到用户登录界面"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        self.driver.find_element_by_link_text('SIGN-OFF').click()
        t=self.driver.current_url
        self.driver.get(t)
        try:
            self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            self.assertTrue(True, msg='case1测试失败')
        self.driver.close()


# 密码输入框是否不支持复制粘贴
#     @unittest.skip('no')
    def test_case2(self):
        """密码输入框是否不支持复制粘贴"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('test123')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(Keys.CONTROL,'a')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(Keys.CONTROL,'c' )
        self.driver.find_element_by_xpath("//input[@name='password']").clear()
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(Keys.CONTROL,'v' )
        t=self.driver.find_element_by_xpath("//input[@name='password']").get_attribute('value')
        self.assertNotEqual(t,'test123', msg='case2测试失败')
        self.driver.close()

# sql注入不知道用户密码密码情况
#     @unittest.skip('no')
    def test_case3(self):
        """sql注入不知道用户密码密码情况"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("\' or 1=1; -- ")
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        try:
            self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case3测试失败')
        self.driver.close()

    # sql注入不知道用户和密码情况
    # @unittest.skip('no')
    def test_case4(self):
        """sql注入不知道用户密码密码情况"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys("\' or 1=1; -- ")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('')
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        try:
            self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case4测试失败')
        self.driver.close()

    # 连续多次登录失败的情况下，系统是否会阻止后续的尝试以应对暴力破解
    def test_case6(self):
        """ 连续多次登录失败的情况下，系统是否会阻止后续的尝试以应对暴力破解"""
        data = {"userName": "mercury",
                "password": "",
                "action": "process",
                "login": "Login"
                }
        session = requests.Session()
        try:
            for i in range(10):
                data["password"]=generate_random_str(6)
                session.post("http://newtours.demoaut.com/login.php",data)
            self.driver.delete_all_cookies()
            self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
            self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
            self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
            self.driver.find_element_by_xpath("//input[@name='login']").click()
            t= self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t=None
        self.assertTrue(t is None, msg='case6测试失败')
        self.driver.close()

# 同一用户先后在多台终端的浏览器上登录，验证登录是否具有互斥性
#     @unittest.skip('no')
    def test_case5(self):
        """同一用户先后在多台终端的浏览器上登录，验证登录是否具有互斥性"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        cook=self.driver.get_cookies()
        print(cook)
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        self.driver.delete_all_cookies()
        self.driver.add_cookie(cook[0])
        self.driver.get("http://newtours.demoaut.com/mercuryreservation.php")
        try:
            t = self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case5测试失败')
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    # reportpath = 'result.html'
    # rs = open(reportpath, 'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=rs,title=u"报告",description=u'123')
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(unittest.makeSuite(Securitytest))
    # runner.run(test_suite)
    # rs.close()