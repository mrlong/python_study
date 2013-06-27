#!/usr/bin/python
# coding=utf-8

# mrlong

import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.163.com'
mail_user = 'mrlong_xp@163.com'
mail_pwd  = 'mrlong7895123'

class sendmailto(object):
	"""docstring for sendmailto"""
	def __init__(self, mailhost,mailuser,mailpwd):
		self.mailhost = mailhost
		self.mailuser = mailuser
		self.mailpwd  = mailpwd

	def send(self,mailto,mailcontent):
		msg = MIMEText(mailcontent,'plain','utf-8')
		msg['From'] = self.mailuser
		msg['Subject']='[提醒邮件]' + mailcontent
		msg['To'] = mailto
		msg['Accept-Language'] = 'zh-CN'
		msg['Accept-Charset'] = 'ISO-8859-1,utf-8'
		try:
			s = smtplib.SMTP()
			s.connect(self.mailhost)
			s.login(self.mailuser,self.mailpwd)
			s.sendmail(self.mailuser,[mailto],msg.as_string()+'\n  {系统自动发送，不必回邮件}')
			s.close()
			print 'success by mail'
		except Exception , e:
			print e

#
#if __name__ == "__main__":
#	mysendmail = sendmailto(mail_host,mail_user,mail_pwd)
#	mysendmail.send('mrlong@qzhsoft.com','test by python 要地要地地一')
#

		
