# coding:utf8
from time import sleep

from uiautomator import device as d

for i in range(0, 10):
    print i
    d.wakeup()

    sleep(10)
    # d.screen.off()
    # sleep(2) #1175 2068 2030 700