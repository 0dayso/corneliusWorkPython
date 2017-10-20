# coding:utf8


from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import datetime

device = MonkeyRunner.waitForConnection(6, "127.0.0.1:62001")
waitTime = 2 # sleep时间，2表示sleep 2 * 30 秒的时间
cityNum = 3 # 几座城市
times = 1 # 运行几次

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

def takeSnapshot():
    image = device.takeSnapshot()
    image.writeToFile('D:/test/images/shot.png')
    MonkeyRunner.sleep(3)

def getSubImage2(name, x, y, x1, y1):
    re = MonkeyRunner.loadImageFromFile('D:/test/images/shot.png')
    re = re.getSubImage((x, y, x1 - x, y1 - y))
    re.writeToFile('D:/test/images/%s.png'%name, 'png')
    sleep(1)

def getSubMenu(x, y, x1, y1):
    re = MonkeyRunner.loadImageFromFile('D:/test/images/shot.png')
    re = re.getSubImage((x, y, x1 - x, y1 - y))
    re.writeToFile('D:/test/images/sub.png', 'png')
    sleep(1)

def getSubImage1(x, y, x1, y1):
    re = MonkeyRunner.loadImageFromFile('D:/test/images/shot.png')
    re = re.getSubImage((x, y, x1 - x, y1 - y))
    re.writeToFile('D:/test/images/sub.png', 'png')
    sleep(1)

def getCityList():
    takeSnapshot()
    getSubImage2("city1", 659, 39, 720, 206)
    getSubImage2("city2", 598, 39, 659, 206)
    getSubImage2("city3", 537, 39, 598, 206)
    # getSubImage2("city4", 476, 39, 537, 206)
    # getSubImage2("city5", 415, 39, 476, 206)
    # getSubImage2("city6", 354, 39, 415, 206)
    # getSubImage2("city7", 293, 39, 354, 206)
    # getSubImage2("city8", 232, 39, 293, 206)

def getMenuIndex():
    sleep(1)
    takeSnapshot()
    getSubMenu(6, 404, 127, 597)
    image1 = MonkeyRunner.loadImageFromFile('D:/test/images/sub.png')
    index = -1
    # menu0:normal, 1:center, 2:兵营, 3:business, 4:bj, 5:bgc
    for i in range(0, 6):
        image2 = MonkeyRunner.loadImageFromFile('D:/test/images/menu_%s.png'%str(i))
        if image1.sameAs(image2, 0.70):
            index = i
            print "same as menu" + str(i)
    if index == 0:
        return 1
    elif index == 1 or index == 2 or index == 3:
        return 3
    elif index == 4 or index == 5:
        return 2
    else:
        return 0


def getCityIndex(num):
    """
    获取num的城市在第几位
    :param num:
    :return: num
    """
    for i in range(1, cityNum + 1):
        image1 = MonkeyRunner.loadImageFromFile('D:/test/images/%s.png'%str(num))
        image2 = MonkeyRunner.loadImageFromFile('D:/test/images/city%s.png'%str(i))
        if image1.sameAs(image2, 0.95):
            return i

def isExistImage(name):
    takeSnapshot()
    getSubImage1(1,2,3,4)
    image1 = MonkeyRunner.loadImageFromFile('D:/test/images/sub.png')
    image2 = MonkeyRunner.loadImageFromFile('D:/test/images/%s.png'%name)
    if image1.sameAs(image2, 0.95):
        return True
    else:
        return False

def startGame():
    """
    判断有没有在
    :return:
    """
    device.wake()
    # 竖屏
    sleep(1)
    touchScreen(70, 237)
    sleep(0.5)
    touchScreen(69, 330)
    for i in range(waitTime):
        sleep(30)
        touchScreen(277, 543)
        print "sleep " + str((i+1) * 30) + " seconds"
    # award()
    # sleep(1)
    backToBattlefield()

def touchScreen(x, y):
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)

def award():
    takeSnapshot()
    getSubImage1(573, 62, 744, 103)
    image1 = MonkeyRunner.loadImageFromFile('D:/test/images/sub.png')
    image2 = MonkeyRunner.loadImageFromFile('D:/test/images/award.png')
    if image1.sameAs(image2, 0.95):
        touchScreen(1069, 80)
        sleep(0.5)

def backToBattlefield():
    takeSnapshot()
    getSubImage1(116, 337,169,545)
    image1 = MonkeyRunner.loadImageFromFile('D:/test/images/sub.png')
    image2 = MonkeyRunner.loadImageFromFile('D:/test/images/backToBattlefield.png')
    isExist = image1.sameAs(image2, 0.95)
    print isExist
    if isExist:
        touchScreen(445, 577)
        sleep(0.5)
        touchScreen(613, 445)
        sleep(10)
    # award()

def cancel():
    touchScreen(438, 438)
    sleep(0.5)

def close():
    touchScreen(1262, 30)
    sleep(1)

def upgradeButton():
    touchScreen(1176, 687)
    sleep(1)
    cancel()

def openCityList():
    touchScreen(44, 521)
    sleep(2)

def selectCity(num1):
    openCityList()
    getCityList()
    num = getCityIndex(num1)
    print "select city " + str(num1) + "; city index " + str(num)
    if num == 1:
        touchScreen(115, 29)
        sleep(10)
    if num == 2:
        touchScreen(115, 90)
        sleep(10)
    if num == 3:
        touchScreen(115, 150)
        sleep(10)
    if num == 4:
        touchScreen(115, 220)
        sleep(10)
    if num == 5:
        touchScreen(115, 280)
        sleep(10)
    if num == 6:
        touchScreen(115, 350)
        sleep(10)
    if num == 7:
        touchScreen(115, 410)
        sleep(10)

def menu(index):
    """
    menu对应的点
    :param index:
    :return:
    """
    if index == 1:
        touchScreen(464, 656)
    elif index == 2:
        touchScreen(556, 655)
    elif index == 3:
        touchScreen(645, 652)
    elif index == 4:
        touchScreen(736, 650)
    elif index == 5:
        touchScreen(823, 650)
    elif index == 6:
        touchScreen(909, 654)
    sleep(1.5)

def city1():
    selectCity(1)
    buildUpgrade(0)
    buildUpgrade(4)
    buildUpgrade(3)
    buildUpgrade(2)
    buildUpgrade(1)
    buildUpgrade(6)
    buildUpgrade(5)
    buildUpgrade(7)
    buildUpgrade(8)
    buildUpgrade(12)
    buildUpgrade(9)
    buildUpgrade(10)
    buildUpgrade(11)


def city2():
    selectCity(2)
    buildUpgrade(0)
    buildUpgrade(4)
    buildUpgrade(3)
    buildUpgrade(2)
    buildUpgrade(1)
    buildUpgrade(6)
    buildUpgrade(5)
    buildUpgrade(7)
    buildUpgrade(8)
    buildUpgrade(12)
    buildUpgrade(9)
    buildUpgrade(10)
    buildUpgrade(11)


def city3():
    selectCity(3)
    buildUpgrade(0)
    buildUpgrade(4)
    buildUpgrade(3)
    buildUpgrade(2)
    buildUpgrade(1)
    # buildUpgrade(6)
    # buildUpgrade(5)
    # buildUpgrade(7)
    # buildUpgrade(8)
    buildUpgrade(12)
    buildUpgrade(9)
    buildUpgrade(10)
    buildUpgrade(11)

def city4():
    selectCity(4)
    buildUpgrade(0)
    buildUpgrade(4)
    buildUpgrade(3)
    buildUpgrade(2)
    buildUpgrade(1)
    buildUpgrade(6)
    buildUpgrade(5)
    buildUpgrade(7)
    buildUpgrade(8)
    buildUpgrade(12)
    buildUpgrade(9)
    buildUpgrade(10)
    buildUpgrade(11)


def city5():
    selectCity(5)
    buildUpgrade(0)
    buildUpgrade(4)
    buildUpgrade(3)
    buildUpgrade(2)
    buildUpgrade(1)
    buildUpgrade(6)
    buildUpgrade(5)
    buildUpgrade(7)
    buildUpgrade(8)
    buildUpgrade(12)
    buildUpgrade(9)
    buildUpgrade(10)
    buildUpgrade(11)


def city6():
    selectCity(6)
    buildUpgrade(0)
    buildUpgrade(4)
    buildUpgrade(3)
    buildUpgrade(2)
    buildUpgrade(1)
    buildUpgrade(6)
    buildUpgrade(5)
    buildUpgrade(7)
    buildUpgrade(8)
    buildUpgrade(12)
    buildUpgrade(9)
    buildUpgrade(10)
    buildUpgrade(11)


def city7():
    selectCity(7)
    buildUpgrade(0)
    buildUpgrade(4)
    buildUpgrade(3)
    buildUpgrade(2)
    buildUpgrade(1)
    buildUpgrade(6)
    buildUpgrade(5)
    buildUpgrade(7)
    buildUpgrade(8)
    buildUpgrade(12)
    buildUpgrade(9)
    buildUpgrade(10)
    buildUpgrade(11)

def buildUpgrade(index):
    num = 0
    if index == 0:# city
        touchScreen(617, 365)
        num = getMenuIndex()
    elif index == 1:# nc
        touchScreen(788, 360)
        num = getMenuIndex()
    elif index == 2:#gt
        touchScreen(769, 438)
        num = getMenuIndex()
    elif index == 3:#xj
        touchScreen(670, 500)
        num = getMenuIndex()
    elif index == 4:#sy
        touchScreen(611, 565)
        num = getMenuIndex()
    elif index == 5:#by
        touchScreen(477, 528)
        num = getMenuIndex()
    elif index == 6:#bgc
        touchScreen(385, 457)
        num = getMenuIndex()
    elif index == 7:#jc
        touchScreen(559, 462)
        num = getMenuIndex()
    elif index == 8:#bj
        touchScreen(449, 352)
        num = getMenuIndex()
    elif index == 9:#fy
        touchScreen(521, 294)
        num = getMenuIndex()
    elif index == 10:#fy
        touchScreen(615, 258)
        num = getMenuIndex()
    elif index == 11:#fy
        touchScreen(734, 285)
        num = getMenuIndex()
    elif index == 12:#business
        touchScreen(833, 564)
        num = getMenuIndex()
    if num > 0:
        sleep(1)
        menu(num)
        upgradeButton()


def task():
    startGame()
    startTime()
    # city1(chi)
    city2()
    city3()
    # city4(chi)
    # city5(chi)
    # city6(chi)
    # city7(chi)
    endTime()
    home()


if __name__ == '__main__':
    ti = times + 1
    # task()
    # sleep(120 * 60)
    for t in range(1, ti):
        print "============start " + str(t) + " time============"
        # if t == 2:
        #     sleep(120 * 60)
        task()
        if t == ti - 1:
            break
        else:
            print "============ END ============"
            # if ti < 10:
            sleep(30 * 60)
            # elif ti < 20:
            #     sleep(20 * 60)
            # else:
            #     sleep(30 * 60)
    print "TOTAL END"

