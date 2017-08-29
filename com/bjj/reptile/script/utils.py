# coding:utf8


from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time

device = MonkeyRunner.waitForConnection()

def sleep(seconds):
    MonkeyRunner.sleep(seconds)

def home():
    device.press('KEYCODE_HOME','DOWN_AND_UP')
    sleep(1)

def startGame():
    device.wake()
    sleep(1)
    device.touch(451, 408,MonkeyDevice.DOWN_AND_UP)
    sleep(0.5)
    device.touch(277, 543,MonkeyDevice.DOWN_AND_UP)
    for i in range(30):
        sleep(2)
        device.touch(277, 543,MonkeyDevice.DOWN_AND_UP)
        print "sleep " + str(i * 2) + " seconds"
    # 点掉所有的框
    device.touch(1069, 80,MonkeyDevice.DOWN_AND_UP)
    sleep(0.5)
    # 进入游戏
    device.touch(420, 325,MonkeyDevice.DOWN_AND_UP)
    sleep(0.5)
    # 点掉所有的框
    device.touch(1069, 80,MonkeyDevice.DOWN_AND_UP)
    sleep(0.5)

def upgradeCity():
    device.touch(617, 365,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(658, 648,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(1178, 691,MonkeyDevice.DOWN_AND_UP)
    sleep(1)

def upgradeFarm():
    device.touch(788, 360,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(478, 654,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(1178, 691,MonkeyDevice.DOWN_AND_UP)
    sleep(1)

def upgradeIron():
    device.touch(769, 438,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(478, 654,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(1178, 691,MonkeyDevice.DOWN_AND_UP)
    sleep(1)

def upgradeRubber():
    device.touch(670, 500,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(478, 654,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(1178, 691,MonkeyDevice.DOWN_AND_UP)
    sleep(1)

def upgradePetroleum():
    device.touch(611, 565,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(478, 654,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(1178, 691,MonkeyDevice.DOWN_AND_UP)
    sleep(1)

def upgradeFactory():
    device.touch(385, 457,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(557, 650,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(1178, 691,MonkeyDevice.DOWN_AND_UP)
    sleep(1)

def upgradeBarracks():
    device.touch(477, 528,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(650, 646,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    device.touch(1178, 691,MonkeyDevice.DOWN_AND_UP)
    sleep(1)


def selectCity(num):
    device.touch(44, 521,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    if num == 1:
        device.touch(115, 29,MonkeyDevice.DOWN_AND_UP)
        sleep(10)
    if num == 2:
        device.touch(115, 90,MonkeyDevice.DOWN_AND_UP)
        sleep(10)
    if num == 3:
        device.touch(115, 150,MonkeyDevice.DOWN_AND_UP)
        sleep(10)
    if num == 4:
        device.touch(115, 220,MonkeyDevice.DOWN_AND_UP)
        sleep(10)
    if num == 5:
        device.touch(115, 280,MonkeyDevice.DOWN_AND_UP)
        sleep(10)
    if num == 6:
        device.touch(115, 350,MonkeyDevice.DOWN_AND_UP)
        sleep(10)
    if num == 7:
        device.touch(115, 410,MonkeyDevice.DOWN_AND_UP)
        sleep(10)

def start(num):
    startGame()
    for i in range(1, num + 1):
        selectCity(i)
        upgradeCity()
        upgradePetroleum()
        upgradeRubber()
        upgradeIron()
        upgradeFarm()
        upgradeFactory()
        upgradeBarracks()

if __name__ == '__main__':
    time.sleep(20 * 60)

    for t in range(1, 10):
        start(3)
        time.sleep(60 * 60)






