"""
@author:luokaiyao
@function:通过ping扫描存活主机
@refer: https://blog.csdn.net/zheng_ruiguo/article/details/84563433

"""
import os
import platform


class PingScan():

    def get_os(self):
        return platform.system()

    # def ping_scan(self, ip):
    #     os_name =  get_os()
    #     if os_name == "Windows":
    #         os.system("ping -n 1" + ip)
    #     if os_name == "Linux":
    #         os.system("ping -c 1 " + ip)





