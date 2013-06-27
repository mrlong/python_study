#!/usr/bin/python
# coding=utf-8
import threading, datetime, logging, time
 
class Scheduler(object):
 
    def schedule(self,trigger,func):
        '''将func任务放入调度列表，根据trigger触发运行
        '''
        pass
 
    def start(self):
        '''开启调度
        '''
        pass
 
    def stop(self):
        '''关闭调度
        '''
        pass
 
class SimpleScheduler(Scheduler):
    def __init__(self):
        self.tasks = []
        self.isRun = False
 
    def schedule(self,trigger,func):
        '''将func任务放入调度列表，根据trigger触发运行
        #    参数说明:
        #    trigger:    允许 字符串（触发表达式）或者继承了Trigger的类
        #                当为字符串时，与linux 的crontab相似
        #                   如："15 12 * * *" 五部分，分别为： 分，时，日，月， 周（周为1至7，周一为1， 周日为7）
        #                   用空格隔开。
        #                    
        #                    支持的特殊字条：
        #                    * 代表任何，  
        #                    , 表示多个情况，   15,16,17 表示三个都可以
        #                    - 表示范围  1-10
        #                    */5 表示每隔5单位时间
        #
        #    func:    可执行的函数
        '''
        if(type(trigger) == type("")):
            self.tasks.append([CronTrigger(trigger),func])
        else:
            self.tasks.append([trigger,func])
 
    def stop(self):
        self.isRun = False
 
    def start(self):
        self.isRun = True
        timer = threading.Timer(1, self._run)
        timer.start()
 
    def _run(self):
        while(self.isRun):
            now = datetime.datetime.now()
            logging.debug("SimpleScheduler: %d:%d" %(now.hour,now.minute))
            self._schedule(now)
            time.sleep(60)
 
    def _schedule(self,now):
        for task in self.tasks:
            try:
                if task[0].trigger(now):
                    self._doTask(now,task[1])
            except Exception,e:
                logging.error(str(e))
 
    def _doTask(self,now,func):
        logging.info('do task: time=%s,func=%s' % (now.isoformat(' '),func.func_name))
        timer = threading.Timer(1, func)
        timer.start()
 
class Trigger(object):
    def trigger(self,time):
        return False
 
class CronTrigger(Trigger):
    def __init__(self, exp):
        if len(exp.split(' ')) != 5 :
            raise Exception('the expression is error : ' + exp) 
        try:
            self._analyzeExp(exp.split(' '))
        except Exception,e:
            raise Exception('the expression is error : ' + exp) 
 
    def trigger(self, time):
        nows = [time.isoweekday(),time.month, time.day, time.hour, time.minute]
        nows.reverse()
        result = [n in t for (n,t) in zip(nows,self.triggers)]
        return all(result) 
 
    def _analyzeExp(self, exp):
        self.triggers = []
        self.triggers.append(self._analyzeSingle(exp[0],0,59))
        self.triggers.append(self._analyzeSingle(exp[1],0,23))
        self.triggers.append(self._analyzeSingle(exp[2],1,31))
        self.triggers.append(self._analyzeSingle(exp[3],1,12))
        self.triggers.append(self._analyzeSingle(exp[4],1,7))
 
    def _analyzeSingle(self, single, min, max):
        if single == '*' :
            return range(min,max+1)
        elif ',' in single:
            return [int(x) for x in single.split(',')]
        elif '-' in single:
            parts = single.split('-')
            maxPart = max
            if int(parts[1]) < maxPart:
                maxPart = int(parts[1])
            minPart = min
            if int(parts[0]) > minPart:
                minPart = int(parts[0])
            return range(minPart, maxPart+1)
        elif '*/' in single:
            den = int(single[2:])
            return [x for x in range(min,max+1) if x%den == 0]
        else :
            return [int(single),]


def printtime():
    print datetime.datetime.now()


if __name__ == "__main__":
    printtime()
    s = SimpleScheduler()
    s.schedule('*/1 * * * *',printtime)
    s.start()
    