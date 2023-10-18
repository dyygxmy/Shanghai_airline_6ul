#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import socket

class dyUdp(threading.Thread):
    def __init__(self, threadID, threadName, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.delay = delay
        self.server_address = ('192.168.1.1', 6666)
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.data = ""

    def sendUdp(self,data):
        self.data = data

    def run(self):
        while 1:
            print(self.threadID,self.threadName,"run","cycle:",self.delay)
            if len(self.data) > 0:
                self.udp_socket.sendto(self.data, self.server_address)
                self.data = ""
                data, server_address = self.udp_socket.recvfrom(1024)
                print('UDP Client Received Data From Server: ', data,server_address)
            time.sleep(self.delay)

# udp = dyUdp(1, "udp", 1)
# udp.start()