#-*-coding:utf-8-*-
from itertools import izip
from PIL import Image


def cropImage(s):
    im = Image.open('C:\\Users\\ShineMo-177\\Desktop\\log\\y\\%s.png'%s)

    box = (417, 608, 687, 695)

    region = im.crop(box)

    region.save('E:\\workspace\\corneliusWorkPython\\snapshot\\s%s.png'%s)
    return 'E:\\workspace\\corneliusWorkPython\\snapshot\\s1.png'


def compareImage():
    i1 = Image.open('E:\\workspace\\corneliusWorkPython\\snapshot\\s4.png')
    i2 = Image.open('E:\\workspace\\corneliusWorkPython\\snapshot\\s5.png')

    # assert i1.mode == i2.mode, "Different kinds of images."
    # assert i1.size == i2.size, "Different sizes."

    pairs = izip(i1.getdata(), i2.getdata())

    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    print "Difference (percentage):", (dif / 255.0 * 100) / ncomponents
    return (dif / 255.0 * 100) / ncomponents

if __name__ == '__main__':
    # compareImage()

    cropImage(7)
    cropImage(8)