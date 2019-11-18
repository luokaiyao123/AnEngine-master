import queue
import threading
from core.multi_threads import MutltThreading
from config.global_config import LOCAL_THREAD_LIST

t = threading.Thread()
lock = threading.Lock()


# 队列列表,用于处理队列行为
class QueueList():
    # 初始化队列
    def __init__(self, size=10):
        self.q = queue.Queue()
        self.size = size

    # 添加进程
    def add_queue(self, t):
        lock.acquire()
        self.q.put(t)
        lock.release()

    # 清理进程
    def clear_queue(self):
        self.q.empty()


if __name__ == '__main__':
    threads = LOCAL_THREAD_LIST
    [threads.append(MutltThreading(i, "name" + str(i), i).start()) for i in range(0, 11)]
    QueueList().add_queue()
