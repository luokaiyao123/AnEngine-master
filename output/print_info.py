from config import global_config
from tool import time_tool

TYPE = ["txt", "word", "excel"]


class PrintConsole():

    def __init__(self):
        self.type = "txt"

    def print2_text(self, name, info):
        dir = global_config.LOG_DIR
        file = open(dir + name + ".txt", 'a')
        file.write(info)
        print("done")

    def print2_word(self, name, info):
        print("word")

    def print2_excel(self):
        print("excel")


if __name__ == '__main__':
    PrintConsole().print2_text("test", "hello")
