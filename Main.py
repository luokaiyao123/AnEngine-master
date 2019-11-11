from core import argparse
from output.log import log

#初始化

def init():
    #初始化菜单
    args = argparse.main()

    #初始化漏洞列表
    init_poc()

    log("Angine Start")


def init_poc():
    print("init_poc")

def _set_Value(value):
    print(value)
