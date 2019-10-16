# -*- coding: utf-8 -*-
# By:CSDN Eastmount 2019-10-05
import threading
import Queue
import sys
from subprocess import Popen, PIPE

#定义一个类 传入参数queue
class DoRun(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        #非空取数据
        while not self._queue.empty():
            ip = self._queue.get()
            #print ip
            check_ping = Popen("ping {0} \n".format(ip), stdin=PIPE, stdout=PIPE,  shell=True)
            data = check_ping.stdout.read()
            if 'TTL' in data:
                sys.stdout.write(ip+' is UP.\n')
            
def main():
    threads = []
    threads_count = 100
    queue = Queue.Queue()
    
    #放入ip地址
    for i in range(1, 255):
        queue.put('1.31.128.' + str(i))

    for i in range(threads_count):
        threads.append(DoRun(queue))

    for i in threads:
        i.start()

    for i in threads:
        i.join()

if __name__ == '__main__':
    main() 
