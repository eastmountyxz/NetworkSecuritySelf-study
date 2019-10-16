# -*-  coding: utf-8 -*-
import requests
from Queue import Queue
import sys
import threading

#多线程实现Web目录扫描
class DirScan(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        #获取队列中的URL
        while not self._queue.empty():
            url = self._queue.get()
            #print url

            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
                }
                #发送请求
                r = requests.get(url=url, headers=headers, timeout=8)
                
                #Web目录存在
                if r.status_code == 200:
                    #print '[*] ' + url
                    sys.stdout.write('[*] %s\n' % url)
            except Exception, e:
                #print e
                pass

#定义队列及放入URL
def start(url, ext, count):
    queue = Queue()

    f = open('%s.txt' % ext, 'r')
    for i in f:
        queue.put(url + i.rstrip('\n'))

    #多线程
    threads = []
    thread_count = int(count)

    for i in range(thread_count):
        threads.append(DirScan(queue))
        
    for t in threads:
        t.start()

    for t in threads:
        t.join()

#主函数
if __name__ == '__main__':
    url = 'http://www.xxxx.com' #网址换成自己的
    ext = 'asp'
    count = 10
    start(url, ext, count)
