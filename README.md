### web_UI自动化框架说明
本框架结合单元测试框架pytest+allure

#### 框架介绍：

目录：

case： 存储测试用例

conftest.py :设置前置操作

            目前框架前置操作：打开浏览器操作，登录操作，谷歌无界面模式操作，allure保存失败用例截图操作

commmon：存储封装的公共方法

        base:封装公共方法（查找元素，输入操作，点击操作，鼠标操作，js处理等等）
        driver:封装浏览器驱动（目前封装了谷歌，火狐，ie浏览器）
        log:输出日志
        read_yaml：读取yaml文件
data：存放测试数据

lib: 存放第三方浏览器驱动

logs: 存放输出的日志文件

pages: 存放测试页面元素，元素操作，断言

report: 存放测试报告

getpathinfo.py :封装路径

pytest.int :配置文件

requirement.txt: 本地python包（pip install -r requirements.txt）

run_main.py: 运行文件

####结构设计

1.每一个页面的所有用例组合在一个测试类里面生成一个py文件

2.将每个页面用例的操作元素，操作步骤封装在一个测试类里面生成一个py文件

3.将测试数据，定位元素存放在yml文件中

4.通过allure生成测试报告

#### 不同前置使用方法：
        在测试类中调用不同的前置方法
        调用打开浏览器前置：
        def test_success_login(self,open_browser,username,password,msg):
            driver = open_browser
        调用谷歌无界面模式前置：
        def test_fail_login(self,driver,username,password,msg):
            #driver调用前置无界面模式启动
            #driver = Base().chromeDriver
            #driver = open_browser
            web = LoginPage(driver)
        调用登录前置：（失败用例就会截图存储到allure报告中）
        def test_new_repository(self,login_fixtrue,msg):
            driver = login_fixtrue
 #### 不同浏览器使用方法：
        driver = WDriver().chromeDriver()
        调用driver.py文件中不同的方法







