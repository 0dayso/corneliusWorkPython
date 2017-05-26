#! usr/bin/python
# coding:UTF-8
import re

s = """



"""


pattern = re.compile('<div id="content">(.*?)</div>', re.S)
items = re.findall(pattern, s)
s = items[0].replace("<br />", "").replace("<br>", "").replace("&nbsp;", "").replace("*", "")
if s.find("ps:"):
    s = "11"

print s