'''
Code description: 登录页面
Create time: 2020/12/14
Developer: 叶修
'''

from common.base import Base
from common.driver import WDriver
from common.read_yml import ReadYaml
testelement = ReadYaml("login_page.yml").get_yaml_data()

class LoginPage(Base):

    #定位元素
    loc1 = tuple(testelement["login_element"][0])#用户名
    loc2 = tuple(testelement["login_element"][1])#密码
    loc3 = tuple(testelement["login_element"][2])#登录按钮
    # 断言元素
    loc4 = tuple(testelement["login_element"][3])#登录成功断言
    loc5 = tuple(testelement["login_element"][4])#登录失败断言

    def input_username(self, text="hanxi978@163.com"):
        '''输入用户名'''
        self.input(self.loc1, text)

    def input_password(self, text="123456"):
        '''输入密码'''
        self.input(self.loc2, text)

    def click_button(self):
        '''点击登录按钮'''
        self.click(self.loc3)

    def login(self, user="hanxi978@163.com", password="123456"):
        '''登录'''
        self.driver.get(self.base_url)
        self.input_username(user)
        self.input_password(password)
        self.click_button()

    def is_login_success(self, expect_text='Working with a team?'):
        text = self.get_text(self.loc4)
        self.log.info("获取到断言元素的文本内容：%s"%text)
        return expect_text == text

    def is_login_fail(self, expect_text='Incorrect username or password.'):
        text = self.get_text(self.loc5)
        self.log.info("获取到断言元素的文本内容：%s"%text)
        return expect_text in text

if __name__ == '__main__':
    # from selenium import webdriver
    # driver = webdriver.Chrome()
    # web = LoginPage(driver)
    driver = WDriver().chromeDriver()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()
    result = web.is_login_success()
    print("登录结果：", result)
    assert result
    driver.quit()
