'''
Code description: 登录页面
Create time: 2020/12/14
Developer: 叶修
'''

import allure
import pytest
from common.base import Base
from common.log import Log
from common.read_yml import ReadYaml
from pages.login_page import LoginPage
from selenium import webdriver
testdata = ReadYaml('login_page.yml').get_yaml_data()#读取数据


@allure.feature("功能点：用户登录页面")
class Test_login():

    log = Log()

    @allure.story("用例：用户登录")
    @pytest.mark.parametrize("username,password,msg",testdata["login_success_data"],
                             ids = ["正确用户名密码登录"])
    #@pytest.mark.skip('跳过该成功用例')
    @pytest.mark.run(order=-1)#调整登录成功用例最后运行
    def test_success_login(self,open_browser,username,password,msg):
        driver = open_browser
        #driver = Base().driver
        web = LoginPage(driver)
        web.login(user=username,password=password)
        with allure.step("获取结果: 获取页面实际结果，判断是否登录成功"):
            result = web.is_login_success(expect_text=msg)
            self.log.info("登录结果：%s"%result)
        with allure.step("断言：判断是否登录成功"):
            assert result
        #driver.quit()

    @allure.story("用例：用户登录")
    @pytest.mark.parametrize("username,password,msg", testdata["login_fail_data"],
                             ids=["错误用户名正确密码登录"])
    # @pytest.mark.skip('跳过')
    def test_fail_login(self,open_browser,username,password,msg):
        #driver调用前置无头模式启动
        driver = open_browser
        web = LoginPage(driver)
        web.login(user=username,password=password)
        with allure.step("获取结果: 获取页面实际结果，判断是否登录成功"):
            result = web.is_login_fail(expect_text=msg)
            self.log.info("登录结果:%s"%result)
        with allure.step("断言：判断是否登录成功"):
            assert result
        #driver.quit()
