#! usr/bin/python
# coding:UTF-8

ss = """
s
"""

s =  ss.replace("<br />", "") \
    .replace("&nbsp;&nbsp;&nbsp;&nbsp;", "  \n") \
    .replace("*", "").replace("…", "")
s = s.lower()

s1 = s[:50]
s2 = s[50:]
# print s
# print s1 + s2
if s2.find("ps:")!=-1:
    print s1 + s2[:s2.index("ps:")]
else:
    print s

print s.strip()