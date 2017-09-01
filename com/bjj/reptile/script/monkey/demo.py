import os,time,profile
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()
print 'connected'
REPEAT_TIME = 50
device.wake()
MonkeyRunner.sleep(3)
device.press('KEYCODE_HOME','DOWN_AND_UP')
MonkeyRunner.sleep(3)





# time1 = 3.71 #3.859
# for i in range(1, REPEAT_TIME):
#     print i
#     time1 += 0.01
#     print "time1: " + str(time1)
#     device.drag((361,1177),(361,1177),time1,1)
#     MonkeyRunner.sleep(3.5)
#     device.touch(353,881,MonkeyDevice.DOWN_AND_UP)
#     MonkeyRunner.sleep(0.5)
