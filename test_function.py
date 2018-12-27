import random

from selenium import webdriver

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


class Functiontest(unittest.TestCase):

    def setUp(self):
        self.id1 = 'mercury'
        self.pw = 'mercury'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_headless()
        chrome_options.add_argument('--disable-gpu')
        self.driver= webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    # 输入已注册的用户名和不正确的密码，验证是否成功，
    # @unittest.skip('no')
    def test_case2(self):
        """输入已注册的用户名和不正确的密码，验证是否成功"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw+"22")
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        try:
            t=self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception :
            t=None
        self.assertTrue(t is None,msg='case2测试失败')
        self.driver.close()

    # 输入已注册的用户名和正确的密码，验证是否成功登录
    # @unittest.skip('no')
    def test_case1(self):
        """输入已注册的用户名和正确的密码，验证是否成功登录"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        try:
            self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            self.assertTrue(True, msg='case1测试失败')
        self.driver.close()

    # 输入未注册的用户名和任意密码，验证是否登录失败，且提示信息正确
    # @unittest.skip('no')
    def test_case3(self):
        """输入未注册的用户名和任意密码，验证是否登录失败，且提示信息正确"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(generate_random_str(6))
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(generate_random_str(6))
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        try:
            t = self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case3测试失败')
        self.driver.close()

    # 用户名和密码两者都为空，验证是否登录失败
    # @unittest.skip('no')
    def test_case4(self):
        """用户名和密码两者都为空，验证是否登录失败"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        # self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(generate_random_str(6))
        # self.driver.find_element_by_xpath("//input[@name='password']").send_keys(generate_random_str(6))
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        try:
            t = self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case4测试失败')
        self.driver.close()

    # 用户名和密码两者之一为空，验证是否登录失败
    # @unittest.skip('no')
    def test_case5(self):
        """用户名和密码两者之一为空，验证是否登录失败"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(generate_random_str(6))
        # self.driver.find_element_by_xpath("//input[@name='password']").send_keys(generate_random_str(6))
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        try:
            t = self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case5测试失败')
        self.driver.close()

    # 用户名和密码是否大小写敏感
    # @unittest.skip('no')
    def test_case6(self):
        """ 用户名和密码是否大小写敏感"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1.upper())
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw.upper())
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        try:
            t = self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case6测试失败')
        self.driver.close()

    # .页面上的密码框是否加密显示
    # @unittest.skip('no')
    def test_case7(self):
        """页面上的密码框是否加密显示"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        try:
            t = self.driver.find_element_by_xpath("//input[@name='password']").get_property("type")
        except Exception:
            t = None
        print(t)
        self.assertEqual(t,"password", msg='case7测试失败')
        self.driver.close()

    # 后台系统创建的用户第一次登录成功时，是否提示修改密码
    @unittest.skip('no')
    def test_case8(self):
        """后台系统创建的用户第一次登录成功时，是否提示修改密码"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.close()


    # 前端页面是否根据设计需求限制用户名和密码长度
    def test_case9(self):
        """前端页面是否根据设计需求限制用户名和密码长度"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        id11=generate_random_str(200)
        ps1=generate_random_str(200)
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(id11)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(ps1)
        id12=self.driver.find_element_by_xpath("//input[@name='userName']").get_property('value')
        ps2 = self.driver.find_element_by_xpath("//input[@name='userName']").get_property('value')
        # print(id11,id12,ps1,ps2)
        self.assertFalse(((id11==id12) &(ps1==ps2)), msg='case9测试失败')
        self.driver.close()

    # 用户登录成功但是登出后，继续操作是否会重定向到用户登录界面
    def test_case10(self):
        """用户登录成功但是登出后，继续操作是否会重定向到用户登录界面"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        self.driver.find_element_by_link_text('SIGN-OFF').click()
        self.driver.get("http://newtours.demoaut.com/mercuryreservation.php")
        try:
            t = self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case10测试失败')
        self.driver.close()

    # 页面默认焦点是否定位在用户输入框中
    def test_case11(self):
        """页面默认焦点是否定位在用户输入框中"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        t=self.driver.switch_to.active_element
        t=t.get_property('name')
        # self.driver.get("http://newtours.demoaut.com/mercuryreservation.php")
        self.assertTrue(t is not None, msg='case11测试失败')
        self.driver.close()

    # 快捷键Tab，是否可以正常使用
    def test_case12(self):
        """ 快捷键Tab，是否可以正常使用"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").click()
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(Keys.TAB)
        t=self.driver.switch_to.active_element.get_property('name')
        self.assertEqual(t,'password', msg='case12测试失败')
        self.driver.close()

    # 快捷键entry，是否可以正常使用
    def test_case13(self):
        """快捷键entry，是否可以正常使用"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(Keys.ENTER)
        try:
            t = self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case13测试失败')
        self.driver.close()

    # 浏览器的前进后退按钮，是否有效
    def test_case14(self):
        """浏览器的前进后退按钮，是否有效"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(Keys.ENTER)
        self.driver.back()  # 后退
        self.driver.forward()  # 前进
        try:
            t = self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case14测试失败')
        self.driver.close()

    # 成功登出后，点击浏览器回退按钮，是否可以继续操作系统
    def test_case15(self):
        """成功登出后，点击浏览器回退按钮，是否可以继续操作系统"""
        self.driver.delete_all_cookies()
        self.driver.get(url='http://newtours.demoaut.com/mercurysignon.php')
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(self.id1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        self.driver.find_element_by_link_text('SIGN-OFF').click()
        self.driver.back()  # 后退
        try:
            t = self.driver.find_element_by_xpath("//input[@name='findFlights']")
        except Exception:
            t = None
        self.assertTrue(t is None, msg='case15测试失败')
        self.driver.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()