# -*- coding: UTF-8 -*-
from pylog import Pylog
import configparser
import sys

def get_config(firstLine=None, secondLine=None):
    config = configparser.ConfigParser()
    # 读取配置文件信息
    config.read('./config.conf', encoding="utf-8")
    try:
        return config[firstLine][secondLine]
    except Exception as e:
        Pylog.error(e)

if __name__ == "__main__":
    mode =get_config("mode","runmode")
    print(mode)