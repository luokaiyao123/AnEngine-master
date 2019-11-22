# 全局字典设置类

global VULN_LIST
VULN_LIST = []


def init():
    global _global_dict
    _global_dict = {}


# 加载添加模块
def add_vuln_list(object):
    if object in VULN_LIST:
        return

    VULN_LIST.append(object)
    set_value("vuln_list", VULN_LIST)


def get_vuln_list():
    return VULN_LIST


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue
