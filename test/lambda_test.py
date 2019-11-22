import unittest



#lambda 以及map的使用
def map_test():
    p = lambda x: x + 1
    print(map(p, [1, 2, 3, 4, 5]))


# lambda 函数练习,lambda 可以构造lambda函数
def lambda_test1():
    p = lambda x, y: x + y
    print(p(4, 6))
    # [i for i in range(0, 10)]
    # print("test")


def _test():
    print("test")


if __name__ == '__main__':
    # lambda_test1()
    map_test()
