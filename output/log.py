from output.print_info import PrintConsole
from tool import time_tool
from core.enums import LOG_LEVEL
from core.enums import LOG_TYPE


def log_web_info(info,level="info"):
    log(info,type=LOG_TYPE.WEB)

def log_system_info(info,level="info"):
    log(info, type=LOG_TYPE.SYSTEM)

def log(info, level="info",type=LOG_TYPE.APP):
    """打印日志，并且以时间为文件名"""
    namestr = time_tool.get_local_datestr()
    str = info + "   " + level + "   " + time_tool.get_local_timestr() + "\n"
    PrintConsole().print2_text(namestr, str)



if __name__ == '__main__':
    log("hello", LOG_LEVEL.ERROR)
