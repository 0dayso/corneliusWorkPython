# coding:utf8


# from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from itertools import izip
import time
from PIL import Image

# device = MonkeyRunner.waitForConnection()
# result = device.takeSnapshot()
#
# result.writeToFile("E:\\workspace\\corneliusWorkPython\\snapshot\\s.png", 'png')
#
# im = Image.open('E:\\workspace\\corneliusWorkPython\\snapshot\\s.png')
im = Image.open('C:\\Users\\ShineMo-177\\Desktop\\log\\y\\Screenshot_20170823-092140.png')

box = (417, 608, 961, 714)

region = im.crop(box)

region.save('E:\\workspace\\corneliusWorkPython\\snapshot\\s1.png')

# result1 = MonkeyRunner.loadImageFromFile('E:\\workspace\\corneliusWorkPython\\snapshot\\s1.png','png')
# result2 = MonkeyRunner.loadImageFromFile('E:\\workspace\\corneliusWorkPython\\snapshot\\s2.png','png')

i1 = Image.open('E:\\workspace\\corneliusWorkPython\\snapshot\\s1.png')
i2 = Image.open('E:\\workspace\\corneliusWorkPython\\snapshot\\s2.png')

assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."

pairs = izip(i1.getdata(), i2.getdata())

if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

ncomponents = i1.size[0] * i1.size[1] * 3
print "Difference (percentage):", (dif / 255.0 * 100) / ncomponents