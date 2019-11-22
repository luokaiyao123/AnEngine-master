import threading
import queue

thread_lock = threading.Lock()


# 多线程处理
class MutltThreading(queue.Queue):

    def __init__(self, queue):
        self.thread_list = []
        threading.Thread.__init__(self)
        self.q = queue

    def _add_thread(self, queue):
        thread_lock.acquire()
        t = queue.get(block=True, timeout=1)
        t.setDaemon(True)
        t.start()
        thread_lock.release()
        self.thread_list.append(t)


    def _start_thread(self, queue):
        map(self._add_thread, [t for t in range(queue)])
        while True:
            alive = False
            for t in self.thread_list:
                alive = alive or t.isAlive()
            if not alive: break


if __name__ == '__main__':
    # t = MutltThreading(1, "test")
    # t.run()
    threads = []
    # 批量添加线程池,开启的进制
    [threads.append(MutltThreading(i, "name" + str(i)).start()) for i in range(0, 11)]
    # [t.join() for t in threads]
    print("end")
