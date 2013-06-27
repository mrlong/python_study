#!/usr/bin/python
# coding=utf-8

import os
import sys
import urllib2
import urllib

os.chdir('/Users/mac-mrlong/DownLoads')
os.getcwd()

a=urllib.urlopen('http://www.qzhsoft.com')

f=open('a.html','wb');
f.write(a.read());
f.close();
print ("saved!");


h4=u'http://www.qzhsoft.com'
h4=h4.encode('utf-8');
print h4
urllib2.urlopen(h4)






