# -*- coding: UTF-8 -*-
import logging
import time

class Pylog:
    def __init__(self):
        ##############################日志配置############################################################
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            # filename="./log/"+ time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+".log",
                            filename="./Report/test.log",
                            filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        ###################################################################################################

    @staticmethod
    def info(data = None):
        logging.info(data)

    @staticmethod
    def debug(data = None):
        logging.debug(data)

    @staticmethod
    def error(data = None):
        logging.error(data)
    @staticmethod
    def warning(data = None):
        logging.warning(data)


if __name__ == "__main__":
    a = Pylog()
    Pylog.info("12345678")