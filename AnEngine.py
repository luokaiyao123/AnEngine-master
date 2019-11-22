import Main
import os
ver = "1.0"
logo = """AnEngine {}""".format(ver)


def main():
    print(logo)
    # 加载主程序
    # curPath = os.path.abspath(os.path.dirname(__file__))

    Main.init(os.getcwd())

if __name__ == '__main__':
    main()

