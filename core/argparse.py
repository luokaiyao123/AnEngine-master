import argparse
import sys
from scan.dir_scan import DirScan
from scan.ping_scan import *


def main(path):
    # dest 相关参数配置项
    # 如何规范参数 设置参数
    parser = argparse.ArgumentParser(description="args")
    # parser.add_argument('-h',type=str,help="help")
    parser.add_argument('-t', type=int, dest='thread', default=5, help="thread count")
    parser.add_argument('-v', '--version', dest='version', action='store_true')
    parser.add_argument('--vuln', type=str, nargs='+', dest='vuln', help="check vuln")
    parser.add_argument('--dir_scan', type=str, dest='dirscan', help="scan dir task")
    parser.add_argument('--config', type=str, dest='config', help='set config file')


    args = parser.parse_args()

    print(len(sys.argv))

    if len(sys.argv) < 2:
        # print("hello")
        # print(args)
        return
    if args.version:
        print("version")
    if args.thread:
        print("thread")
    if args.dirscan:
        # 确定扫描类型
        # DirScan.scan_common_dir(str(args[2]), path)
        # if sys.argv == "Ping":
        #     PingScan().run()
        # if sys.argv == "Port":
        #     print("port")
        pass

    # 菜单选项

    # 通过 vars 返回字典属性值
    return vars(args)


if __name__ == '__main__':
    # print(globals())
    main()
