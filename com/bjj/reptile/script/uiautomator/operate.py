# coding:utf8

from itertools import izip
from PIL import Image
from time import sleep
from uiautomator import device as d

waitTime = 6

def compareImage(path):
    i1 = Image.open('E:\\workspace\\corneliusWorkPython\\snapshot\\snapshot.png')
    i2 = Image.open(path)

    # assert i1.mode == i2.mode, "Different kinds of images."
    # assert i1.size == i2.size, "Different sizes."

    pairs = izip(i1.getdata(), i2.getdata())

    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    component = i1.size[0] * i1.size[1] * 3
    print "Difference (percentage):", (dif / 255.0 * 100) / component
    return (dif / 255.0 * 100) / component

def isSame(name):
    d.screenshot("E:\\workspace\\corneliusWorkPython\\snapshot\\snapshot.png")
    # result.writeToFile("E:\\workspace\\corneliusWorkPython\\snapshot\\snapshot.png", 'png')
    sleep(1.5)

    if name == "only":
        im = Image.open("E:\\workspace\\corneliusWorkPython\\snapshot\\snapshot.png")
        box = (417, 608, 599, 695)
        region = im.crop(box)
        region.save("E:\\workspace\\corneliusWorkPython\\snapshot\\snapshot1.png")
    else:
        im = Image.open("E:\\workspace\\corneliusWorkPython\\snapshot\\snapshot.png")
        box = (417, 608, 687, 695)
        region = im.crop(box)
        region.save("E:\\workspace\\corneliusWorkPython\\snapshot\\snapshot1.png")
    component = 0.0
    if name == "city":
        path = "E:\\workspace\\corneliusWorkPython\\snapshot\\city.png"
        component = compareImage(path)
    elif name == "by" or name == "jc":
        path = "E:\\workspace\\corneliusWorkPython\\snapshot\\by.png"
        component = compareImage(path)
    elif name == "gc":
        path = "E:\\workspace\\corneliusWorkPython\\snapshot\\gc.png"
        component = compareImage(path)
    elif name == "business":
        path = "E:\\workspace\\corneliusWorkPython\\snapshot\\business.png"
        component = compareImage(path)
    elif name == "bj":
        path = "E:\\workspace\\corneliusWorkPython\\snapshot\\bj.png"
        component = compareImage(path)
    elif name == "only":
        path = "E:\\workspace\\corneliusWorkPython\\snapshot\\only.png"
        component = compareImage(path)
    if component < 0.4:
        return True
    else:
        return False

def home():
    d.press.home()
    sleep(1)

def startGame():
    d.wakeup()
    d.click(256, 1123)
    sleep(1)
    d.click(451, 408)
    sleep(0.5)
    d.click(277, 543)
    for i in range(waitTime):
        sleep(10)
        d.click(277, 543)
        print "sleep " + str((i+1) * 10) + " seconds"
    # 点掉所有的框
    d.click(1069, 80)
    sleep(1)
    # 进入游戏
    d.click(420, 325)
    sleep(10)
    # 点掉所有的框
    d.click(1069, 80)
    sleep(0.5)

def close():
    d.click(1262, 30)
    sleep(1)

def upgradeButton():
    d.click(1176, 687)
    sleep(1.5)

def upgradeCity():
    d.click(617, 365)
    sleep(1)
    if isSame("city"):
        print "upgradeCity"
        menu(3)
        upgradeButton()

def selectCity(num):
    print "select city " + str(num)
    d.click(44, 521)
    sleep(2)
    if num == 1:
        d.click(115, 29)
        sleep(15)
    if num == 2:
        d.click(115, 90)
        sleep(15)
    if num == 3:
        d.click(115, 150)
        sleep(15)
    if num == 4:
        d.click(115, 220)
        sleep(15)
    if num == 5:
        d.click(115, 280)
        sleep(15)
    if num == 6:
        d.click(115, 350)
        sleep(15)
    if num == 7:
        d.click(115, 410)
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
        d.click(788, 360)
        sleep(1)
    elif index == 2:
        d.click(769, 438)
        sleep(1)
    elif index == 3:
        d.click(670, 500)
        sleep(1)
    elif index == 4:
        d.click(611, 565)
        sleep(1)
    elif index == 5:
        d.click(477, 528)
        sleep(1)
    elif index == 6:
        d.click(385, 457)
        sleep(1)
    elif index == 7:
        d.click(559, 462)
        sleep(1)
    elif index == 8:
        d.click(449, 352)
        sleep(1)
    elif index == 9:
        d.click(521, 294)
        sleep(1)
    elif index == 10:
        d.click(615, 258)
        sleep(1)
    elif index == 11:
        d.click(734, 285)
        sleep(1)
    elif index == 12:
        d.click(833, 564)
        sleep(1)


    if name == "nc":
        if isSame("only"):
            print "upgrade farm"
            menu(1)
            upgradeButton()
    elif name == "t":
        if isSame("only"):
            print "upgrade Iron"
            menu(1)
            upgradeButton()
    elif name == "xj":
        if isSame("only"):
            print "upgrade xj"
            menu(1)
            upgradeButton()
    elif name == "sy":
        if isSame("only"):
            print "upgrade sy"
            menu(1)
            upgradeButton()
    elif name == "by":
        if isSame("by"):
            print "upgrade binY"
            menu(3)
            upgradeButton()
    elif name == "gc":
        if isSame("gc"):
            print "upgrade bgc"
            menu(2)
            upgradeButton()
    elif name == "bj":
        if isSame("bj"):
            print "upgrade buJiChang"
            menu(2)
            upgradeButton()
    elif name == "business":
        if isSame("business"):
            print "upgrade business"
            menu(3)
            upgradeButton()
    elif name == "jc":
        if isSame("jc"):
            print "upgrade airport"
            menu(3)
            upgradeButton()
    elif name == "fy":
        if isSame("only"):
            print "upgrade fy"
            menu(1)
            upgradeButton()
    elif name == "cj":
            print "cj"
            menu(1)
            d.click(800, 461)

def menu(index):
    """
    menu对应的点
    :param index:
    :return:
    """
    if index == 1:
        d.click(464, 656)
    elif index == 2:
        d.click(556, 655)
    elif index == 3:
        d.click(645, 652)
    elif index == 4:
        d.click(736, 650)
    elif index == 5:
        d.click(823, 650)
    elif index == 6:
        d.click(909, 654)
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
    upgrade(12, "business")

def city2():
    selectCity(2)
    upgrade(0, "")
    upgrade(4, "sy")
    upgrade(3, "xj")
    upgrade(2, "t")
    upgrade(1, "nc")
    upgrade(12, "business")

def city3():
    selectCity(3)
    upgrade(0, "")
    upgrade(4, "sy")
    upgrade(3, "xj")
    upgrade(2, "t")
    upgrade(1, "nc")
    upgrade(6, "gc")
    upgrade(5, "by")
    upgrade(12, "business")

def city4():
    selectCity(4)
    upgrade(0, "")
    upgrade(2, "sy")
    upgrade(11, "xj")
    upgrade(3, "t")
    upgrade(7, "nc")
    upgrade(12, "gc")
    upgrade(10, "by")

def city5():
    selectCity(5)
    upgrade(0, "")
    upgrade(1, "cj")
    upgrade(2, "cj")
    upgrade(3, "cj")
    upgrade(4, "cj")
    upgrade(5, "cj")
    upgrade(6, "cj")
    upgrade(7, "cj")
    upgrade(8, "cj")
    upgrade(9, "cj")
    upgrade(10, "cj")
    upgrade(11, "cj")
    upgrade(12, "cj")

def task():
    startGame()
    city1()
    city2()
    city3()
    city4()
    # city5()
    home()
    d.sleep()

def task1():
    startGame()
    selectCity(1)
    upgrade(4, "sy")
    home()
    d.sleep()

if __name__ == '__main__':
    sleep(60 * 60)
    for i in range(0, 10):
        task()
        sleep(60 * 60)
