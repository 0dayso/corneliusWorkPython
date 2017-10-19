# coding:utf8


from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import datetime

device = MonkeyRunner.waitForConnection(6, "127.0.0.1:62001")
# MonkeyRunner.sleep(1)
# image = device.takeSnapshot()
# MonkeyRunner.sleep(1)


# image.writeToFile('D:/test/images/black.png')

# result = MonkeyRunner.loadImageFromFile('D:/test/images/1.png')
# result1 = MonkeyRunner.loadImageFromFile('D:/test/images/black.png')
# result1 = result1.getSubImage((599,197,88,108))
# result1.writeToFile('D:/test/images/1.png')

def takeSnapshot1():
    image = device.takeSnapshot()
    image.writeToFile('D:/test/images/shot.png')
    MonkeyRunner.sleep(1)

def getSubImage1(x, y, x1, y1):
    re = MonkeyRunner.loadImageFromFile('D:/test/images/shot.png')
    re = re.getSubImage((x, y, x1 - x, y1 - y))
    re.writeToFile('D:/test/images/sub.png')

def getSubImage2(name, x, y, x1, y1):
    re = MonkeyRunner.loadImageFromFile('D:/test/images/1/%s.png'%name)
    re = re.getSubImage((x, y, x1 - x, y1 - y))
    re.writeToFile('D:/test/images/%s_1.png'%name)

def isExistImage(name):
    takeSnapshot1()
    getSubImage1(1,2,3,4)
    image1 = MonkeyRunner.loadImageFromFile('D:/test/images/sub.png')
    image2 = MonkeyRunner.loadImageFromFile('D:/test/images/%s.png'%name)
    if image1.sameAs(image2, 0.95):
        return True
    else:
        return False






if __name__ == '__main__':
    # getSubImage2('shot1', 6, 404, 127, 1051)
    getSubImage2('shot1', 6, 404, 127, 597)
    getSubImage2('shot2', 6, 404, 127, 597)
    getSubImage2('shot3', 6, 404, 127, 597)
    getSubImage2('shot4', 6, 404, 127, 597)
    getSubImage2('shot5', 6, 404, 127, 597)
    getSubImage2('shot6', 6, 404, 127, 597)
    getSubImage2('shot7', 6, 404, 127, 597)
    getSubImage2('shot8', 6, 404, 127, 597)
    getSubImage2('shot9', 6, 404, 127, 597)
    getSubImage2('shot10', 6, 404, 127, 597)

    # image1 = MonkeyRunner.loadImageFromFile('D:/test/images/menu_center1.png')
    # image2 = MonkeyRunner.loadImageFromFile('D:/test/images/menu_center.png')
    # print image1.sameAs(image2, 0.99)
    print 'end'







