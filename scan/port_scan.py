import socket
from dic import port_dic



def port_scan(ip, port, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        return True
    except:
        return False

    # try:
    #     s.send('')
    #     r = s.recv(512)
    #     s.close()
    #     return True
    # except:
    #     pass


def common_scan(ip):
    common_ports = port_dic.COMMON_PORT
    for i in range(0, len(common_ports)):
        # print(COMMON_PORT[i])
        flag = port_scan(ip, common_ports[i])
        # print(flag)
        if (flag):
            print("[+] port {} is open".format(common_ports[i]))


if __name__ == '__main__':
    common_scan("192.168.3.52")
