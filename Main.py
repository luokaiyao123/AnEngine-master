from core import argparse
from output.log import log
from config.global_config import VULN_LIST
from poc import poc_demo
from poc import poc_demo2

#初始化

def init():
    #初始化菜单
    args = argparse.main()

    #初始化漏洞列表
    init_poc()

    # log("Angine Start")



def init_poc():
    """注册加载漏洞列表"""
    globals()['vuln'] = VULN_LIST
    print(globals()['vuln'])




def _set_Value(value):
    print(value)
