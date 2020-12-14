'''
Code description: 运行测试用例
Create time: 2020/11/5
Developer: 李万洋
'''
import os
import pytest
if __name__ == '__main__':
    pytest.main(['-s', '--alluredir', 'report/tmp'])#-m运行mark标记文件
    os.system('allure generate report/tmp -o report/html --clean') # /report/tmp 为存放报告的源文件目录
