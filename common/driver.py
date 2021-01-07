'''
Code description: 封装浏览器驱动
Create time: 2020/12/14
Developer: 李万洋
'''
import os
import sys
import getpathinfo
from selenium import webdriver
from common.log import Log

class WDriver(object):

    log = Log()
    path = getpathinfo.get_path()  # 获取本地路径
    chromedriver_filepath = os.path.join(path, 'lib') + '/' + 'chromedriver.exe'  # 拼接定位到存储第三方chromedriver.exe
    msedgedriver_filepath = os.path.join(path, 'lib') + '/' + 'msedgedriver.exe' #拼接定位到存储第三方msedgedriver.exe
    # Firefox driver
    def fireFoxDriver(self):
        """
        :return:
        """
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            self.log.info('FireFoxDriverServer.exe executable needs to be in PATH. Please download!')
            raise e
        else:
            self.log.info('%s:found the Firefox driver [%s] successed !' %(sys._getframe().f_code.co_name,self.driver))
            return self.driver

    # chrome driver
    def chromeDriver(self):
        """
        :return:
        """
        try:
            #修改下载文件位置
            # chromeOptions = webdriver.ChromeOptions()
            # prefs = {"download.default_directory": "F:\\TestDownloads"}
            #chromeOptions.add_experimental_option("prefs", prefs)
            #self.driver = webdriver.Chrome(chrome_options=chromeOptions)
            self.driver = webdriver.Chrome(self.chromedriver_filepath)
        except Exception as e:
            self.log.info('ChromeDriverServer.exe executable needs to be in PATH. Please download!')
            raise e
        else:
            self.log.info('%s:found the chrome driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.driver


    # msedge driver
    def msedgeDriver(self):
        """
        :return:
        """
        try:
            self.driver = webdriver.Edge(self.msedgedriver_filepath)
        except Exception as e:
            self.log.info('IEDriverServer.exe executable needs to be in PATH. Please download!')
            raise e
        else:
            self.log.info('%s:found the IE driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.driver


if __name__ == '__main__':
    WDrive=WDriver()
    #WDrive.chromeDriver()
    WDrive.msedgeDriver()