'''
Code description:注册
Create time: 2020/12/14
Developer: 叶修
'''

from common.base import Base
from common.read_yml import ReadYaml
testelement = ReadYaml("register_page.yml").get_yaml_data()

class Register_Page(Base):

    #定位元素
    loc1 = tuple(testelement["register_element"][0])  # 注册
    loc2 = tuple(testelement["register_element"][1])  # 登录名
    loc3 = tuple(testelement["register_element"][2])  # 用户名
    loc4 = tuple(testelement["register_element"][3])  # 密码
    loc5 = tuple(testelement["register_element"][4])  # 确认密码
    # 断言元素
    loc6 = tuple(testelement["register_element"][5])  # 成功断言
    loc7 = tuple(testelement["register_element"][6])  # 失败断言

    def click_register(self):
        '''点击注册,进入注册页面'''
        self.driver.get(self.base_url)
        self.click(self.loc1)

    def input_loginname(self, text="Mrqiu"):
        '''输入登录名'''
        self.input(self.loc2, text)

    def input_username(self, text="Mrqiu"):
        '''输入用户名'''
        self.input(self.loc3, text)

    def input_password(self, text="668566"):
        '''输入密码'''
        self.input(self.loc4, text)

    def input_repassword(self, text="668566"):
        '''输入确认密码'''
        self.input(self.loc5, text)

    def click_register_2(self):
        '''点击注册'''
        self.click(self.loc1)

    def register_success(self, expect_text='welcome'):
        text = self.get_text(self.loc6)
        self.log.info("获取到断言元素的文本内容：%s"%text)
        return expect_text in text

    def register_fail(self, expect_text='用户已存在'):
        text = self.get_text(self.loc7)
        self.log.info("获取到断言元素的文本内容：%s" % text)
        return expect_text in text

if __name__ == '__main__':
    pass
