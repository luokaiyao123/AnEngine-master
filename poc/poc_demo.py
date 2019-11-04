import requests
from tool import request_tool


class PocDemo():

    def __init__(self):
        pass

    def get_info(self):
        info = {
            "name": "Weblogic弱口令",
            "desc": "攻击者通过此漏洞可以登陆管理控制台，通过部署功能可直接获取服务器权限。",
            "level": "高危",
            "type": "弱口令",
            "author": "wolf@YSRC",
            "refer": ["http://jingyan.baidu.com/article/c74d6000650d470f6b595d72.html"],
            "keyword": "tag:weblogic",
            "source": 1
        }
        return info


    def check(self,ip,port,timeout=5):
        header = request_tool.get_request_headers()
        url = "http://{}:{}".format(ip,port)
        # req = requests.get(url=url,header=header)
        # payload = ""
        print(url)
        print(header)

#注册全局环境变量
globals()['POC_Check'] = PocDemo

if __name__ == '__main__':
    poc = PocDemo()
    poc.check("192.168.1.1",8080)