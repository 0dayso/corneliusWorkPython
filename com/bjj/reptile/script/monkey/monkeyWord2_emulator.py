# coding:utf8


from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import datetime

device = MonkeyRunner.waitForConnection()
waitTime = 2 # sleep时间，2表示sleep 2 * 30 秒的时间

def startTime():
    now = datetime.datetime.now()
    print "start time " + now.strftime('%Y-%m-%d %H:%M:%S')

def endTime():
    now = datetime.datetime.now()
    print "end time " + now.strftime('%Y-%m-%d %H:%M:%S')

def sleep(seconds):
    MonkeyRunner.sleep(seconds)

def home():
    device.press('KEYCODE_HOME','DOWN_AND_UP')
    sleep(1)

def cancel():
    device.touch(438, 438, MonkeyDevice.DOWN_AND_UP)
    sleep(0.5)

def startGame():
    device.wake()
    sleep(1)
    device.touch(70, 237, MonkeyDevice.DOWN_AND_UP)
    sleep(0.5)
    device.touch(69, 330, MonkeyDevice.DOWN_AND_UP)
    for i in range(waitTime):
        sleep(30)
        device.touch(277, 543,MonkeyDevice.DOWN_AND_UP)
        print "sleep " + str((i+1) * 30) + " seconds"
    # 点掉所有的框
    device.touch(1069, 80,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    # 进入游戏
    device.touch(420, 325,MonkeyDevice.DOWN_AND_UP)
    sleep(10)
    # 点掉所有的框
    device.touch(1069, 80,MonkeyDevice.DOWN_AND_UP)
    sleep(0.5)

def close():
    device.touch(1262, 30, MonkeyDevice.DOWN_AND_UP)
    sleep(1)

def upgradeButton():
    device.touch(1176, 687, MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    cancel()

def upgradeCity():
    device.touch(617, 365,MonkeyDevice.DOWN_AND_UP)
    sleep(1)
    print "upgradeCity"
    menu(3)
    upgradeButton()

def selectCity(num):
    print "select city " + str(num)
    device.touch(44, 521,MonkeyDevice.DOWN_AND_UP)
    sleep(2)
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

def upgrade(index, name, chi):
    """
    nc, t, xj, sy, by, gc, bj, business, jc, fy
    :param index:
    :param name:
    :return:
    """
    if index == 0:
        # if chi % 2 == 0 or chi == 0:
        #     upgradeCity()
        upgradeCity()
    elif index == 1:
        device.touch(788, 360,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 2:
        device.touch(769, 438,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 3:
        device.touch(670, 500,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 4:
        device.touch(611, 565,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 5:
        device.touch(477, 528,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 6:
        device.touch(385, 457,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 7:
        device.touch(559, 462,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 8:
        device.touch(449, 352,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 9:
        device.touch(521, 294,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 10:
        device.touch(615, 258,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 11:
        device.touch(734, 285,MonkeyDevice.DOWN_AND_UP)
        sleep(1)
    elif index == 12:
        device.touch(833, 564,MonkeyDevice.DOWN_AND_UP)
        sleep(1)

    if name == "nc":
        print "upgrade farm"
        menu(1)
        upgradeButton()
    elif name == "t":
        print "upgrade Iron"
        menu(1)
        upgradeButton()
    elif name == "xj":
        print "upgrade xj"
        menu(1)
        upgradeButton()
    elif name == "sy":
        print "upgrade sy"
        menu(1)
        upgradeButton()
    elif name == "by":
        print "upgrade binY"
        menu(3)
        upgradeButton()
    elif name == "gc":
        print "upgrade bgc"
        menu(2)
        upgradeButton()
    elif name == "bj":
        print "upgrade buJiChang"
        menu(2)
        upgradeButton()
    elif name == "business":
        print "upgrade business"
        menu(3)
        upgradeButton()
    elif name == "jc":
        print "upgrade airport"
        menu(3)
        upgradeButton()
    elif name == "fy":
        print "upgrade fy"
        menu(1)
        upgradeButton()

def menu(index):
    """
    menu对应的点
    :param index:
    :return:
    """
    if index == 1:
        device.touch(464, 656, MonkeyDevice.DOWN_AND_UP)
    elif index == 2:
        device.touch(556, 655, MonkeyDevice.DOWN_AND_UP)
    elif index == 3:
        device.touch(645, 652, MonkeyDevice.DOWN_AND_UP)
    elif index == 4:
        device.touch(736, 650, MonkeyDevice.DOWN_AND_UP)
    elif index == 5:
        device.touch(823, 650, MonkeyDevice.DOWN_AND_UP)
    elif index == 6:
        device.touch(909, 654, MonkeyDevice.DOWN_AND_UP)
    sleep(1.5)

#     nc, t, xj, sy, by, gc, bj, business, jc, fy
def city1(chi):
    selectCity(1)
    upgrade(0, "", chi)
    # upgrade(4, "sy", chi)
    # upgrade(3, "xj", chi)
    upgrade(2, "t", chi)
    upgrade(1, "nc", chi)
    upgrade(6, "gc", chi)
    upgrade(5, "by", chi)
    # upgrade(7, "jc", chi)
    # upgrade(8, "bj", chi)
    # upgrade(9, "fy", chi)
    # upgrade(10, "fy", chi)
    # upgrade(11, "fy", chi)
    # upgrade(12, "business", chi)

def city2(chi):
    selectCity(2)
    upgrade(0, "", chi)
    upgrade(4, "sy", chi)
    upgrade(3, "xj", chi)
    upgrade(2, "t", chi)
    upgrade(1, "nc", chi)
    # upgrade(6, "gc", chi)
    # upgrade(5, "by", chi)
    # upgrade(7, "jc", chi)
    # upgrade(8, "bj", chi)
    upgrade(12, "business", chi)
    # upgrade(9, "fy", chi)
    # upgrade(10, "fy", chi)
    # upgrade(11, "fy", chi)


def city3(chi):
    selectCity(3)
    upgrade(0, "", chi)
    upgrade(4, "sy", chi)
    upgrade(3, "xj", chi)
    upgrade(2, "t", chi)
    upgrade(1, "nc", chi)
    # upgrade(6, "gc", chi)
    # upgrade(5, "by", chi)
    # upgrade(7, "jc", chi)
    # upgrade(8, "bj", chi)
    upgrade(12, "business", chi)
    # upgrade(9, "fy", chi)
    # upgrade(10, "fy", chi)
    # upgrade(11, "fy", chi)

def city4(chi):
    selectCity(4)
    upgrade(0, "", chi)
    upgrade(4, "sy", chi)
    upgrade(3, "xj", chi)
    upgrade(2, "t", chi)
    upgrade(1, "nc", chi)
    # upgrade(6, "gc", chi)
    # upgrade(5, "by", chi)
    # upgrade(7, "jc", chi)
    # upgrade(8, "bj", chi)
    upgrade(12, "business", chi)
    # upgrade(9, "fy", chi)
    # upgrade(10, "fy", chi)
    # upgrade(11, "fy", chi)


def city5(chi):
    selectCity(5)
    upgrade(0, "", chi)
    upgrade(4, "sy", chi)
    upgrade(3, "xj", chi)
    upgrade(2, "t", chi)
    upgrade(1, "nc", chi)
    # upgrade(6, "gc", chi)
    # upgrade(5, "by", chi)
    # upgrade(7, "jc", chi)
    # upgrade(8, "bj", chi)
    upgrade(12, "business", chi)
    # upgrade(9, "fy", chi)
    # upgrade(10, "fy", chi)
    # upgrade(11, "fy", chi)


def city6(chi):
    selectCity(6)
    upgrade(0, "", chi)
    upgrade(3, "sy", chi)
    upgrade(5, "xj", chi)
    upgrade(9, "t", chi)
    upgrade(2, "nc", chi)
    # upgrade(6, "gc", chi)
    # upgrade(5, "by", chi)
    # upgrade(7, "jc", chi)
    # upgrade(8, "bj", chi)
    # upgrade(9, "fy", chi)
    # upgrade(10, "fy", chi)
    # upgrade(11, "fy", chi)
    upgrade(1, "business", chi)


def city7(chi):
    selectCity(7)
    # upgrade(0, "", chi)
    upgrade(9, "sy", chi)
    upgrade(4, "xj", chi)
    upgrade(12, "t", chi)
    upgrade(1, "nc", chi)
    # upgrade(6, "gc", chi)
    # upgrade(5, "by", chi)
    # upgrade(7, "jc", chi)
    # upgrade(8, "bj", chi)
    # upgrade(9, "fy", chi)
    # upgrade(10, "fy", chi)
    # upgrade(11, "fy", chi)
    upgrade(6, "business", chi)



def task(chi):
    startGame()
    startTime()
    city1(chi)
    # city2(chi)
    # city3(chi)
    # city4(chi)
    # city5(chi)
    # city6(chi)
    # city7(chi)
    endTime()
    home()


if __name__ == '__main__':
    ti = 30
    # task()
    # sleep(120 * 60)
    for t in range(1, ti):
        print "============start " + str(t) + " time============"
        # if t == 2:
        #     sleep(120 * 60)
        task(t)
        if t == ti - 1:
            break
        else:
            print "============ END ============"
            sleep(10 * 60)
    print "TOTAL END"






