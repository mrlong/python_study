#!/usr/bin/python
# coding=utf-8
__author__ = 'clownfish'

import urllib2,urllib,cookielib,json
#from sendmailto import sendmail
import sendmail

username = "mrlong.com@gmail.com"
password = "mrlong7895123"

class sign(object):
    #username = 'mrlong.com@gmail.com'
    #password = 'mrlong7895123'
    #登录显示页面
    indexurl = 'https://www.kuaipan.cn/account_login.htm'
    #登录的form表单url
    loginurl = 'https://www.kuaipan.cn/index.php?ac=account&op=login'
    #签到的真正url
    signurl = 'http://www.kuaipan.cn/index.php?ac=common&op=usersign'


    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self,msg):

        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        msg = "打开登录页面"
        try:
            urllib2.urlopen(self.indexurl)
            post_data = {'username':self.username,'userpwd':self.password,'isajax':'yes'}
            req=urllib2.Request(self.loginurl,urllib.urlencode(post_data))
        except Exception, e:
            msg = msg + "网络链接错误"
            return False
        msg = msg + "登录成功,准备签到！"
        response = urllib2.urlopen(req)
        login=response.read()
        return login

    def sign(self):
        response = urllib2.urlopen(self.signurl)
        sign = response.read()
        l = json.loads(sign)
        if (l and l['state'] == 1) or \
        (l and 0 == l['state'] and l['increase'] * 1 == 0 and l['monthtask'].M900 == 900):
            return "恭喜你签到成功！"
            k = l['increase']*1
            m = l['rewardsize'] * 1
            if (k == 0 and l['monthtask'].M900 == 900):
                return "本月签到积分已领取完成"
            else:
                return "签到奖励积分:%s" % (k)
            if m == 0:
                return "手气太不好了！奖励 0M 空间"
            else:
                return "签到奖励空间：%s" % (m)
        else:
            if (l['state'] == -102):
                return "今天您已经签到过了"
            else:
                return "签到失败，遇到网络错误，请稍后再试！"

        return sign

if __name__ == "__main__":
    sign = sign(username,password)
    msg = ''
    if sign.login(msg):
        msg = msg + sign.sign()

    mail_host = 'smtp.163.com'
    mail_user = 'mrlong_xp@163.com'
    mail_pwd  = 'mrlong7895123'
    mysendmail = sendmail.sendmailto(mail_host,mail_user,mail_pwd)
    mysendmail.send('mrlong@qzhsoft.com','金山快盘'+ msg)

