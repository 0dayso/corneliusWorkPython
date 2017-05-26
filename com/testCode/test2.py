#! usr/bin/python
# coding:UTF-8

s = "ps:sfsaf,21654321阿斯兰肯定附件卡索拉夲 Ps:16565asfdjoaisfj alksjfoa i asl拉克丝地方加拉斯肌肤虽阿里山的风景荔枝百"
s = s.lower()
s1 = s[:20]
s2 = s[20:]
print s
print s1 + s2
if s2.find("ps:"):
    print s1 + s2[:s2.index("ps:")]




