'''
Code description:添加设备
Create time: 2021/3/24
Developer: 叶修
'''
import time

import allure
import pytest
from common.log import Log
from common.read_yml import ReadYaml
from pages.add_equipment_page import Add_Equipment_Page
testdata = ReadYaml('add_equipment_page.yml').get_yaml_data()#读取数据

@allure.feature("功能点：添加设备")
class Test_Add_Equipment():

    log = Log()

    @allure.story("用例：添加设备")
    @pytest.mark.parametrize("name,model,num,brand,version",testdata["equipment_success_data"],
                             ids = ["添加设备"])
    #@pytest.mark.skip('跳过该成功用例')
    def test_add_equipment(self,login_fixtrue,name,model,num,brand,version):
        driver = login_fixtrue
        register = Add_Equipment_Page(driver)
        with allure.step("点击添加设备,跳转添加设备"):
            time.sleep(1)
            register.click_add_equipment()
        with allure.step('输入设备名'):
            time.sleep(1)
            register.input_name(text=name)
        with allure.step('输入型号'):
            register.input_model(text=model)
        with allure.step('输入编号'):
            register.input_num(text=num)
        with allure.step('输入品牌'):
            register.input_brand(text=brand)
        with allure.step('输入系统'):
            register.input_version(text=version)
        with allure.step('点击添加'):
            register.click_add()
        with allure.step("获取结果: 获取页面实际结果，判断是否注册成功"):
            result = register.register_success(expect_text=name)
            self.log.info("获取结果：%s"%result)
        with allure.step("断言：判断是否打开成功"):
            assert result
