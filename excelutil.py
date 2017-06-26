#-*- coding:utf-8 -*-
import xlrd
import json
import csv
import re
import config
from pylog import Pylog
'''获取测试数据'''

class ExcelUtil:
    def __init__(self,file,sheetname):
        self.sheetname = sheetname
        self.dataSheet = xlrd.open_workbook(file).sheet_by_name(sheetname)
        # get titles
        self.row = self.dataSheet.row_values(0)
        # get rows number
        self.rowNum = self.dataSheet.nrows
        # get columns number
        self.colNum = self.dataSheet.ncols
        # the current column
        self.curRowNo = 1

    #获取用例数据
    def get_excel(self):
        var_file = config.get_config("normal","var_file")
        r = []
        while self.hasNext():
            s = {}
            col = self.dataSheet.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]

            #重置用例名称
            s["用例No"] = self.sheetname + str(s["用例No"])

            #引入变量
            if s["输入值"][:2] == "${":
                var = re.findall('{(.*)}', s["输入值"], re.S)[0]
                vars = self.get_var(var=var,var_file=var_file)
                s["输入值"] = vars

            #引入其他用例集
            try:
                if s["动作"] == "引入":
                    file = './data/'+json.loads(s["输入值"])["file"]
                    sheet = json.loads(s["输入值"])["sheet"]
                    aimslist = ExcelUtil(file=file,sheetname=sheet).get_excel()
                    r.extend(aimslist)
                else:
                    r.append(s)
            except Exception as e :
                Pylog.error("引入用例错误..." + str(e) + "|"+ s["输入值"])

            self.curRowNo += 1
        return r
    #遍历
    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    #获取变量
    def get_var(self,var="all_vars",var_file=None):
        dic = {}
        try:
            with open(var_file,'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    dic[row[0]] = row[1]
                if var == "all_vars":
                    return dic
                return dic[var]
        except Exception as e :
            Pylog.error("读取变量错误："+str(e))

if __name__ == "__main__":
    s = ExcelUtil('./data/客户端.xlsx','MG电子').get_excel()
    print(s)