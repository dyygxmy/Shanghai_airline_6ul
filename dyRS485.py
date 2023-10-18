#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

class dyRS485(threading.Thread):
    def __init__(self, threadID, threadName, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.delay = delay

    def run(self):
        while 1:
            print(self.threadID,self.threadName,"run","cycle:",self.delay)
            time.sleep(self.delay)

thread1 = dyRS485(1, "RS485", 2)
thread1.start()