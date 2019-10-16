# -*- coding: utf-8 -*- 
from socket import *
from time import ctime

HOST = 'localhost'          #主机名
PORT =  21567               #端口号
BUFSIZE = 1024              #缓冲区大小1K
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)       #绑定地址到套接字
tcpSerSock.listen(5)        #监听 最多同时5个连接进来

while True:                 #无限循环等待连接到来
    try:
        print 'Waiting for connection ....'
        tcpCliSock, addr = tcpSerSock.accept()  #被动接受客户端连接
        print u'Connected client from : ', addr

        while True:
            data = tcpCliSock.recv(BUFSIZE)     #接受数据
            if not data:
                break
            else:
                print 'Client: ',data
            tcpCliSock.send('[%s] %s' %(ctime(),data)) #时间戳

    except Exception,e:
        print 'Error: ',e
tcpSerSock.close()          #关闭服务器
tcpCliSock.close()
