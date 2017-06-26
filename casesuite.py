# -*- coding: UTF-8 -*-
import unittest
import config
import ddtSelenium
import time
from pylog import Pylog
from action import Action
from predata import Predata

@ddtSelenium.ddt
class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.action = Action()
        # cookies = eval(config.get_config("normal","cookie"))
        # cls.action.driver.driver.add_cookie(cookies)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.action.driver.close()

    @ddtSelenium.data(*Predata().get_data())
    def testcase(self, data):
        Pylog.info(str(data[list(data.keys())[0]]) + "开始")
        if data["动作"] == "等待":
            time.sleep(int(data["输入值"]))
        else:
            text = self.action.pre_do(data)

        if data["动作"] == "断言":
            Pylog.info("断言："+ str(data[list(data.keys())[0]]))
            if text != data["输入值"]:
                Pylog.info("断言截图：" + str(data[list(data.keys())[0]]))
                self.action.driver.save_png('./Report/'+data['用例No']+'.jpg')
            self.assertEqual(text, data["输入值"])