"""
@author:luokaiyao
@function:通过ping扫描存活主机
@refer: https://blog.csdn.net/zheng_ruiguo/article/details/84563433

"""
import os
import platform


class PingScan():

    def __init__(self):
        self.name = u"ping扫描"

    def _get_os(self):
        return platform.system()

    def run(self):
        os = self._get_os()
        print(os)


if __name__ == '__main__':
    test = PingScan().run()





