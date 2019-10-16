# -*- coding: utf-8 -*-
# By:CSDN Eastmount 2019-10-05
import thread
import time
from subprocess import Popen, PIPE

def ping_check(ip):
    check = Popen("ping {0} \n".format(ip), stdin=PIPE, stdout=PIPE, shell=True)
    data = check.stdout.read() #数据
    if 'TTL' in data: #存活
        print '%s is UP' % ip

#主函数
if __name__ == '__main__':
    #寻找目标 ichunqiu  1.31.128.240
    for i in range(1,255):
        ip = '1.31.128.' + str(i)
        #多线程方法
        thread.start_new_thread(ping_check, (ip, ))
        time.sleep(0.1)
