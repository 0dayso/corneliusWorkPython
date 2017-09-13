#! usr/bin/python
# coding:UTF-8
import json

text1 = "D:\\test\\users.txt"
f = open(text1, "r+")
lines = f.readlines()
i = 0
for line in lines:
    if len(line) != 0:
        js = json.loads(line)
        print len(js['data'])

f.close()


# text1 = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\wuCuo\\allChapter.txt"
#
# f = open(text1, "r+")
# lines = f.readlines()
# i = 0
# for line in lines:
#     line = line.split(",")
#     print line[0]
#     i += 1
#     if i==10:
#         break
# f.close()









