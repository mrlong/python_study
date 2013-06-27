#!/usr/bin/python
# coding=utf-8

import socket;

class mysocket(object):
	"""docstring for mysocket"""
	def __init__(self, sock=None):
		super(mysocket, self).__init__()
		if sock is None:
			self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		else:
			self.sock = sock

	def connect(self,host,port):
		self.sock.connect((host,port));


	def sendtest(self,msg):
		totalsent = 0;
		while totalsent <MSGLEN:
			sent = self.sock.send(msg[totalsent:]);
			if sent == 0:
				raise RuntimeError("socket connection brken");
			totalsent = totalsent + sent;


my=mysocket();
my.connect('www.qq.com',80);

# 2 ///////////////////////////////////////////////////
class mytest(object):
	"""docstring for mytest"""
	i=12345;
	def __init__(self, arg):
		super(mytest, self).__init__()
		if arg != None:
			self.i = arg; 

	def geti(self):
		return self.i;

myt = mytest(None);
print myt.geti();


# 3 ////////////////////////////////////////////////////
from socket import * 
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
	print 'waiting for connection....'
	tcpCliSock,addr = tcpSerSock.accept()
	print '...connection from:',addr

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send('[%s] %s' % (ctime(),data))


tcpSerSock.close()



