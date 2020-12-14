'''
Code description:新建储存库
Create time: 2020/12/14
Developer: 李万洋
'''

from common.base import Base
from common.read_yml import ReadYaml
testelement = ReadYaml("new_repository.yml").get_yaml_data()

class New_Repository_Page(Base):

    #定位元素
    loc1 = tuple(testelement["new_repositories_element"][0])#new
    # 断言元素
    loc2 = tuple(testelement["new_repositories_element"][1])#登录成功断言

    def click_new(self):
        '''点击new'''
        self.click(self.loc1)

    def is_open_windows_success(self, expect_text='Create a new repository'):
        text = self.get_text(self.loc2)
        self.log.info("获取到断言元素的文本内容：%s"%text)
        return expect_text == text

if __name__ == '__main__':
    pass
