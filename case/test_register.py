'''
Code description: 用户注册
Create time: 2020/12/14
Developer: 叶修
'''
import time

import allure
import pytest
from faker import Faker

from common.base import Base
from common.log import Log
from common.read_yml import ReadYaml
from pages.register_page import Register_Page
testdata = ReadYaml('register_page.yml').get_yaml_data()#读取数据

@allure.feature("功能点：用户注册")
class Test_Register():

    log = Log()

    @allure.story("用例：用户注册")
    @pytest.mark.parametrize("login_name,user_name,password,repassword,msg",testdata["register_success_data"],
                             ids = ["用户成功注册"])
    #@pytest.mark.skip('跳过该成功用例')
    def test_register(self,open_browser,login_name,user_name,password,repassword,msg):
        driver = open_browser
        register = Register_Page(driver)
        with allure.step("点击注册,跳转注册页"):
            register.click_register()
        fake = Faker(locale='zh_CN')
        num = fake.numerify()
        with allure.step('输入登录名'):
            register.input_loginname(text=login_name+num)
        with allure.step('输入用户名'):
            register.input_username(text=user_name+num)
        with allure.step('输入密码'):
            register.input_password(text=password)
        with allure.step('输入确认密码'):
            register.input_repassword(text=repassword)
        with allure.step('点击注册'):
            register.click_register_2()
        with allure.step("获取结果: 获取页面实际结果，判断是否注册成功"):
            result = register.register_success(expect_text=msg)
            self.log.info("获取结果：%s"%result)
        with allure.step("断言：判断是否打开成功"):
            assert result

    @allure.story("用例：用户注册")
    @pytest.mark.parametrize("login_name,user_name,password,repassword,msg",testdata["register_fail_data_1"],
                             ids = ["用户重复注册"])
    #@pytest.mark.skip('跳过该成功用例')
    def test_new_repository_2(self,open_browser,login_name,user_name,password,repassword,msg):
        driver = open_browser
        register = Register_Page(driver)
        with allure.step("点击注册,跳转注册页"):
            register.click_register()
        with allure.step('输入登录名'):
            register.input_loginname(text=login_name)
        with allure.step('输入用户名'):
            register.input_username(text=user_name)
        with allure.step('输入密码'):
            register.input_password(text=password)
        with allure.step('输入确认密码'):
            register.input_repassword(text=repassword)
        with allure.step('点击注册'):
            register.click_register_2()
        with allure.step("获取结果: 获取页面实际结果，判断是否注册成功"):
            result = register.register_fail(expect_text=msg)
            self.log.info("获取结果：%s"%result)
        with allure.step("断言：判断是否打开成功"):
            assert result

    @allure.story("用例：用户注册")
    @pytest.mark.parametrize("login_name,user_name,password,repassword,msg", testdata["register_fail_data_2"],
                             ids=["新注册用户新旧密码不一致"])
    # @pytest.mark.skip('跳过该成功用例')
    def test_new_repository_3(self, open_browser, login_name, user_name, password, repassword, msg):
        driver = open_browser
        register = Register_Page(driver)
        with allure.step("点击注册,跳转注册页"):
            register.click_register()
        fake = Faker(locale='zh_CN')
        num = fake.numerify()
        with allure.step('输入登录名'):
            register.input_loginname(text=login_name+num)
        with allure.step('输入用户名'):
            register.input_username(text=user_name+num)
        with allure.step('输入密码'):
            register.input_password(text=password)
        with allure.step('输入确认密码'):
            register.input_repassword(text=repassword)
        with allure.step('点击注册'):
            register.click_register_2()
        with allure.step("获取结果: 获取页面实际结果，判断是否注册成功"):
            result = register.register_fail(expect_text=msg)
            self.log.info("获取结果：%s" % result)
        with allure.step("断言：判断是否打开成功"):
            assert result