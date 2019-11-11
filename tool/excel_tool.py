import pandas as pd
from pandas import DataFrame
from config import global_config


def read_excel():
    df = pd.read_excel("new.xlsx")
    print(df)


def write_excel(data,name):
    # data = {
    #     'name': ['张三', '李四', '王五'],
    #     'age': [11, 12, 13],
    #     'sex': ['男', '女', '男'],
    # }

    df = DataFrame(data)
    df.to_excel(global_config.LOG_DIR +  name + ".xlsx",index=False)

def create_format(data):
    map = {}
    ips = []
    port = []
    map['ips'] = data['ip']
    df = pd.DataFrame()
    return df

def test():
    ips = []
    ports = []
    data = {}
    for i in range(0, 10):
        data['ip'] = ips.append(i)
        data['port'] = ports.append(i)

    # print(data)
    print(data)
    df = pd.DataFrame({'ip': ips, 'port': ports})
    print(df)
    # # df.to_csv(path_or_buf='text4.csv', sep=',', na_rep='NA', float_format='%.2f', columns=['a_name', 'b_name'])
    # df.to_excel("test2.xlsx",index=False)
    # write_excel(data, "test")


if __name__ == '__main__':
    # write_excel()
    # read_excel()
    test()