import argparse
import sys
from scan.ping_scan import *

def main():
    # dest 相关参数配置项
    # 如何规范参数 设置参数
    parser = argparse.ArgumentParser(description="args")
    # parser.add_argument('-h',type=str,help="help")
    parser.add_argument('-t',type=int,dest='thread',default=5,help="thread count")
    parser.add_argument('-v','--version',dest='version',action='store_true')
    parser.add_argument('--vuln',type=str,nargs='+', dest='vuln',help="check vuln")
    parser.add_argument('--scan',type=str,dest='scan', help="scan task")
    parser.add_argument('--config',type=str,dest='config',help='set config file')



    args = parser.parse_args()

    print(len(sys.argv))
    # print(args.version)
    # print(args.thread)
    if len(sys.argv) < 2:
        # print("hello")
        # print(args)
        return
    if args.version:
        print("version")
    if args.thread:
        print("thread")
    if args.scan:
        # 确定扫描类型
        if sys.argv == "Ping":
            PingScan().run()
        if sys.argv == "Port":
            print("port")

    #菜单选项


    #通过 vars 返回字典属性值
    return vars(args)


if __name__ == '__main__':
    # print(globals())
    main()



