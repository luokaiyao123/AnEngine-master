import Main
ver = "1.0"
logo = """AnEngine {}""".format(ver)


def main():
    print(logo)
    # 加载主程序
    Main.init()
    # print(globals().keys())

if __name__ == '__main__':
    main()

