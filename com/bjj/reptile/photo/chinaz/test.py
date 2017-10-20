#! usr/bin/python
# coding:UTF-8
import re
import requests
import time


def downloadPic(imageUrl, filePath):
    r = requests.get(imageUrl)
    with open(filePath, "wb") as code:
        code.write(r.content)


if __name__ == '__main__':
    path = 'D:\\0Bjj\Photo\\chinaz\\jiaotonggongju\\'

    f = open('D:\\test\\chinaz\\jiaotonggongju.txt', 'r')
    index = 0
    for line in f.readlines():
        if index < 5:
            line = line.split(',')
            name = line[0].decode('utf-8')
            url = line[1].replace('\n','').replace(' ','')
            print url
            print path + name + '.rar'
            downloadPic(url, path + "123" + '.rar')
            index += 1
            time.sleep(2)
        else:
            break
    f.close()

    # url = 'http://zjyd.sc.chinaz.com/Files/DownLoad/pic9/201710/bpic3779.rar'
    # downloadPic(url, path + "暗示法大" + '.rar')





