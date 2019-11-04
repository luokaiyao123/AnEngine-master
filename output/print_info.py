from config import global_config

TYPE = ["txt", "word", "excel"]


class PrintConsole():

    def __init__(self, type):
        self.type = type

    def print2_text(self, name, info):
        self.type = TYPE[0]
        dir = global_config.LOG_DIR
        file = open(dir + name + ".txt", 'a')
        file.write(info)
        print("done")

    def print2_word(self,name,info):
        print("word")

    def print2_excel(self):
        print("excel")
