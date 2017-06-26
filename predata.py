# -*- coding: UTF-8 -*-
import config
from pylog import Pylog
from excelutil import ExcelUtil
import json


class Predata:
    def __init__(self):
        pass

    def get_data(self):
        datalist = []
        mode = config.get_config("mode", "mode")
        file = config.get_config("normal","file")
        sheet = config.get_config("normal","sheet")
        if mode == "normal":
            datalist = self.get_exceldata(file,sheet)
        return datalist

    def get_exceldata(self,file,sheet):
        datalist =  ExcelUtil(file,sheet).get_excel()
        n = 0
        for item in datalist:
            item["用例No"] = str(10000+n) + item["用例No"]
            n += 1
        return datalist

if __name__ == "__main__":
    s = Predata().get_data()
    print(s)
