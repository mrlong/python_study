#!/usr/bin/python
# coding=utf-8

from socket import *

HOST = ''
PORT = 1234
BUFSIZ = 1024
ADDR = (HOST,PORT)
print ADDR;

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = raw_input('>')
	if not data: 
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data;

tcpCliSock.close()


# while 1:
#     #accept connections from outside
#     (clientsocket, address) = serversocket.accept()
#     #now do something with the clientsocket
#     #in this case, we'll pretend this is a threaded server
#     ct = client_thread(clientsocket)    采用线程来处理服务器接收到的请求。
#     ct.run()

