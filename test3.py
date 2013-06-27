#!/usr/bin/python
# coding=utf-8
# author: 龙仕云  2013－6－7
# 等等

from twisted.internet import protocol,reactor

class Echo(protocol.Protocol):
	def dateReceived(self,data):
		self.transport.write(data)

class EchoFactory(protocol.Factory):
	"""docstring for EchoFactory"""
	def buildProtocal(self,addr):
		return Echo()


reactor.listenTCP(1234,EchoFactory())
reactor.run()
