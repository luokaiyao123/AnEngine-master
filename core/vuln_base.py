# 漏洞基类，用于继承
class VulnBase(object):

    def __init__(self):
        self.name = ""

    #检测方法
    def _check(self):
        pass

    #输出
    def _output(self):
        pass


