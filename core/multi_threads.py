import threading

thread_lock = threading.Lock()


class MutltThreading(threading.Thread):

    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        thread_lock.acquire()
        threading.Thread.run(self)
        # print("%s,%s thread is running" % (self.id, self.name))
        thread_lock.release()


if __name__ == '__main__':
    # t = MutltThreading(1, "test")
    # t.run()
    threads = []
    #批量添加线程池,开启的进制
    [threads.append(MutltThreading(i, "name" + str(i)).start()) for i in range(0, 11)]
    # [t.join() for t in threads]
    print("end")