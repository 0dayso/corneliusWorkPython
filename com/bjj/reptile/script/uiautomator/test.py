# coding:utf8
from time import sleep

from uiautomator import device as d


d.wakeup()
d.screenshot("E:\\workspace\\corneliusWorkPython\\snapshot\\snapshot.png")
sleep(2)
d.sleep()