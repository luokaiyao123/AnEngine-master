#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
from queue import Queue
import os
import platform
from subprocess import PIPE
from config.global_config import SCAN_RESULT

threadlock = threading.Lock()


#ping扫描主机类
class PingScan():
    def __init__(self, ips_list):
        self.thread_list = []
        self._make_queue(ips_list)
        for i in range(10):
            self._start_thread()
        self._check_exit()

    def _ping_scan(self, ip):
        osname = platform.system()
        print(osname + "start scaning ")
        if osname == "nt":
            try:
                # os 打开open管道执行命令
                p= os.popen('ping -n 1 ' + ip,  stdout=PIPE)
            except:
                threadlock.release()
            if p.stdout.read().find("TTL") != -1: SCAN_RESULT.append(ip)
        else:
            try:
                p=os.popen(['ping','-c 1',ip],  stdout=PIPE, stderr=PIPE)

            except:
                threadlock.release()
            if p.stdout.read().find("1 received") != -1: SCAN_RESULT.append(ip)
            threadlock.release()

    def _make_queue(self, ips_list):
        self.q = Queue()
        map(lambda x: self.q.put(x), ips_list)

    def _start_thread(self):
        while not self.q.empty():
            try:
                ip = self.q.get(block = True, timeout = 1)
                self._make_thread(ip)
                #self.q.task_done()
            except KeyboardInterrupt:
                try:
                    threadlock.release()
                except:
                    pass
            except ValueError:
                pass
            except:    
                pass
            try:
                self.q.task_done()
            except:
                pass

    def _make_thread(self, ip):
        threadlock.acquire()
        t = threading.Thread(target=self._ping_scan, args=(ip,))
        t.setDaemon(True)
        t.start()
        self.thread_list.append(t)

    def _check_exit(self):
        while 1:
            alive = False
            for t in self.thread_list:
                alive = alive or t.isAlive()
            if not alive:
                break

if __name__ == '__main__':
    PingScan("192.168.3.52")
    print(SCAN_RESULT)