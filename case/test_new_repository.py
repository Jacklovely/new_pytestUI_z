'''
Code description: 新建储存库
Create time: 2020/12/14
Developer: 叶修
'''

import allure
import pytest

from common.base import Base
from common.log import Log
from common.read_yml import ReadYaml
from pages.new_repository import New_Repository_Page
testdata = ReadYaml('new_repository.yml').get_yaml_data()#读取数据

@allure.feature("功能点：新建储存库")
class Test_New_Repository():

    log = Log()

    @allure.story("用例：新建储存库")
    @pytest.mark.parametrize("msg",testdata["success_data"],
                             ids = ["点击新建储存库"])
    #@pytest.mark.skip('跳过该成功用例')
    def test_new_repository(self,login_fixtrue,msg):
        driver = login_fixtrue
        new_repository = New_Repository_Page(driver)
        with allure.step("点击new"):
            new_repository.click_new()
        with allure.step("获取结果: 获取页面实际结果，判断是否打开新增窗口"):
            result = new_repository.is_open_windows_success(expect_text=msg[0])
            self.log.info("获取结果：%s"%result)
        with allure.step("断言：判断是否打开成功"):
            assert result
        driver.quit()
