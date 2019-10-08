import logging
import os
import time

class LogGen(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        # 设置日志级别
        self.logger.setLevel(logging.INFO)


        lt = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        logname = os.path.dirname(os.path.abspath('.')) + '/logs/' + lt + ".log"


        fileh = logging.FileHandler(logname)
        self.logger.setLevel(logging.INFO)

        consoleh = logging.StreamHandler()
        consoleh.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        fileh.setFormatter(formatter)
        consoleh.setFormatter(formatter)
        self.logger.addHandler(fileh)
        self.logger.addHandler(consoleh)
    def getLog(self):
        return self.logger









