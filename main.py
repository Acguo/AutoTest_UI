# -*- coding: UTF-8 -*-
from pylog import Pylog
logging = Pylog()
import HTMLTestRunner
import unittest
import sys
from casesuite import Case



suite = unittest.TestLoader().loadTestsFromTestCase(Case)
filename = sys.path[0] + "./Report/report.html"
fp = open(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况")
runner.run(suite)
fp.close()
