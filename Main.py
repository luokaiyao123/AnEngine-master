from core import argparse, common
from output.log import log
from config.global_config import VULN_LIST
import os
from core import gobal_dict
import requests


# 初始化
# arg 当前项目根目录
def init(path):

    #加载类库
    init_lib(path)

    # 初始化菜单
    args = argparse.main(path)

    # 初始化漏洞列表
    init_poc()



def init_lib(path):
    """加载类库"""
    # common.compile_file("config.global_config")
    # 加载类库文件
    # globals()['poc'] = os
    # __import__()

    # 初始化全局变量
    gobal_dict.init()
    #设置初始根目录
    gobal_dict.set_value('root',path)
    print("----------------compile poc_demo classes -------------------------")
    # common.compile_file("poc.poc_demo",path)


def init_poc(path):
    """注册加载漏洞列表"""
    # globals()['vuln'] = VULN_LIST
    # print(globals()['POC_Check'])


    # 初始化vulnlist 列表
    VULN_LIST = []
    for vuln_name in VULN_LIST:
        common.compile_file('poc.%s'%(str(vuln_name)))
    poc_path = os.path.join(os.getcwd(), "poc")
    # common.compile_file("poc_demo", poc_path)
    files = []
    # for root, dirs, files in os.walk(poc_path):
    #     # print(file)
    #     for name in files:
    #         common.compile_file(name, poc_path)
    # print(files)

    # print(globals()['POC_Check'])
    # print(poc_path)
    # for i in globals()['vuln']:
    #     print(i)

