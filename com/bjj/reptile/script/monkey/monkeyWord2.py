# coding:utf8


from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()
waitTime = 6

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
    for i in range(waitTime):
        sleep(10)
        device.touch(277, 543,MonkeyDevice.DOWN_AND_UP)
        print "sleep " + str((i+1) * 10) + " seconds"
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
    sleep(1.5)

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
        sleep(15)
    if num == 2:
        device.touch(115, 90,MonkeyDevice.DOWN_AND_UP)
        sleep(15)
    if num == 3:
        device.touch(115, 150,MonkeyDevice.DOWN_AND_UP)
        sleep(15)
    if num == 4:
        device.touch(115, 220,MonkeyDevice.DOWN_AND_UP)
        sleep(15)
    if num == 5:
        device.touch(115, 280,MonkeyDevice.DOWN_AND_UP)
        sleep(15)
    if num == 6:
        device.touch(115, 350,MonkeyDevice.DOWN_AND_UP)
        sleep(15)
    if num == 7:
        device.touch(115, 410,MonkeyDevice.DOWN_AND_UP)
        sleep(15)

def upgrade(index, name):
    """
    nc, t, xj, sy, by, gc, bj, business, jc, fy
    :param index:
    :param name:
    :return:
    """
    if index == 0:
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
def city1():
    selectCity(1)
    upgrade(0, "")
    upgrade(4, "sy")
    upgrade(3, "xj")
    upgrade(2, "t")
    upgrade(1, "nc")
    upgrade(6, "gc")
    upgrade(5, "by")
    upgrade(7, "jc")
    # upgrade(12, "business")

def city2():
    selectCity(2)
    upgrade(0, "")
    upgrade(4, "sy")
    upgrade(3, "xj")
    upgrade(2, "t")
    upgrade(1, "nc")
    # upgrade(12, "business")

def city3():
    selectCity(3)
    upgrade(0, "")
    upgrade(4, "sy")
    upgrade(3, "xj")
    upgrade(2, "t")
    upgrade(1, "nc")
    upgrade(6, "gc")
    upgrade(5, "by")
    # upgrade(12, "business")

def city4():
    selectCity(4)
    upgrade(0, "")
    # upgrade(4, "sy")
    upgrade(11, "xj")
    upgrade(3, "t")
    upgrade(7, "nc")
    upgrade(12, "gc")
    upgrade(10, "by")

def task():
    startGame()
    city1()
    city2()
    city3()
    city4()
    home()

def task1():
    startGame()
    selectCity(1)
    upgrade(4, "sy")
    home()





if __name__ == '__main__':
    task()
    # for t in range(1, 2):
    #     task()
    #     time.sleep(60 * 60)






