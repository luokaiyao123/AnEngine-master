import socket
import os

#检测ip是否有效
def check_ip_valid(ip):
    try:
        for _ in [int(x) for x in ip.split('.')]:
            if _ < 0 or _ > 255:return False
        return True
    except:
        return False

#从url 获取ip信息
def get_ip_by_ip_or_url(url):
    try:
        ip = [socket.gethostbyname(url),]
        return ip
    except:
        # PrintConsole('Failed to parse the target "%s"'%url, 'error')
        raise

def compile_file(file):
    try:
        # 加载路径
        load_path = '%s/%s.py' % (os.getcwd(), file.replace('.', '/'))
        # load_file_path = '%s/%s.py' % (load_file_base_path, load_filename.replace('.', '/'))
        # 读取加载路径的东西
        load_source = open(load_path, encoding='utf-8').read()

        load_code = compile(load_source, load_path, 'exec')
        exec(load_code)
        # 成功加载
        print(globals())
    except:
        raise



if __name__ == '__main__':
    # print(check_ip_valid("9.168.1100.254"))
    print(get_ip_by_ip_or_url("www.baidu.com"))