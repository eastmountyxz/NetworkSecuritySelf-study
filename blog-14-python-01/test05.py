# -*- coding: utf-8 -*- 
from socket import *

HOST = 'localhost'          #主机名
PORT =  21567               #端口号 与服务器一致
BUFSIZE = 1024              #缓冲区大小1K
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)    #连接服务器

while True:                 #无限循环等待连接到来
    try:
        data = raw_input('>')
        if not data:
            break
        tcpCliSock.send(data)            #发送数据
        data = tcpCliSock.recv(BUFSIZE)  #接受数据
        if not data:
            break
        print 'Server: ', data
    except Exception,e:
        print 'Error: ',e
        
tcpCliSock.close()          #关闭客户端
