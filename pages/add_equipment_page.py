'''
Code description:添加设备
Create time: 2021/3/24
Developer: 李万洋
'''

from common.base import Base
from common.read_yml import ReadYaml
testelement = ReadYaml("add_equipment_page.yml").get_yaml_data()

class Add_Equipment_Page(Base):

    #定位元素
    loc1 = tuple(testelement["equipment_element"][0])  # 添加设备
    loc2 = tuple(testelement["equipment_element"][1])  # 设备名
    loc3 = tuple(testelement["equipment_element"][2])  # 型号
    loc4 = tuple(testelement["equipment_element"][3])  # 编号
    loc5 = tuple(testelement["equipment_element"][4])  # 品牌
    loc6 = tuple(testelement["equipment_element"][5])  # 系统
    loc7 = tuple(testelement["equipment_element"][6])  # 系统
    # 断言元素
    loc8 = tuple(testelement["equipment_element"][7])  # 成功断言

    def click_add_equipment(self):
        '''点击添加设备'''
        self.click(self.loc1)

    def input_name(self, text="Mrqiu"):
        '''输入设备名'''
        self.input(self.loc2, text)

    def input_model(self, text="Mrqiu"):
        '''输入型号'''
        self.input(self.loc3, text)

    def input_num(self, text="668566"):
        '''输入编号'''
        self.input(self.loc4, text)

    def input_brand(self, text="668566"):
        '''输入品牌'''
        self.input(self.loc5, text)

    def input_version(self, text="668566"):
        '''输入系统'''
        self.input(self.loc6, text)

    def click_add(self):
        '''点击注册'''
        self.click(self.loc7)

    def register_success(self, expect_text='小米'):
        text = self.get_text(self.loc8)
        self.log.info("获取到断言元素的文本内容：%s"%text)
        return expect_text in text

if __name__ == '__main__':
    pass
