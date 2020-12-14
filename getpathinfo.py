'''
Code description: 封装测试路径
Create time: 2020/12/14
Developer: 李万洋
'''

import os

def get_path():
    curpath = os.path.dirname(os.path.realpath(__file__))
    return curpath

if __name__ == '__main__':
    print("测试路径",get_path())