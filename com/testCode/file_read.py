#! usr/bin/python
# coding:UTF-8

text1 = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\wuCuo\\allChapter.txt"

f = open(text1, "r+")
lines = f.readlines()
i = 0
for line in lines:
    line = line.split(",")
    print line[0]
    i += 1
    if i==10:
        break
f.close()
