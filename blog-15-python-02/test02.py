# -*- coding: utf-8 -*-
# By:CSDN Eastmount 2019-10-05
import thread
import time
from subprocess import Popen, PIPE

def ping_check():
    #check = Popen(['/bin/bash', '-c', 'ping -c 2 ' + '127.0.0.1'], stdin=PIPE, stdout=PIPE)
    ip = '127.0.0.1'
    #ping指定次数后停止ping 但报错访问被拒绝，选项 -c 需要具有管理权限。
    #check = Popen("ping -c 3 {0} \n".format(ip), stdin=PIPE, stdout=PIPE,  shell=True)
    check = Popen("ping {0} \n".format(ip), stdin=PIPE, stdout=PIPE,  shell=True)
    data = check.stdout.read() #数据
    print data

#程序成功在同一时刻运行两个函数
if __name__ == '__main__':
    ping_check()
