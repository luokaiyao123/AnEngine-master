from tool import request_tool
from output import print_info
from config import global_config
ver = "1.0"
logo = """"""


def main():
    log = print_info.PrintConsole(print_info.TYPE[0])
    # globals()['POC_Check']
    # print(globals()['POC_Check'])
    print("")
    html = request_tool.get_web_html("https://baidu.com")
    # print(html)
    log.print_text("html",html)



if __name__ == '__main__':
    main()
