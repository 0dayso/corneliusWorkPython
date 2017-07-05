#! usr/bin/python
# coding:UTF-8
import os



def dealCookie():
    fileName = os.getcwd() + "\\cookie.txt"
    s = ""
    f = open(fileName, "r")
    lines = f.readlines()
    for line in lines:

        if line[0] != '#':
            print line
            if line.find('_scn')!=-1:
                line = line[line.find('_scn'):]
                line = line.replace('\t','').replace('\n','')
                line = line.replace('_scn', '_scn=') + '; '
                s += line
            elif line.find('timeStamp')!=-1:
                line = line[line.find('timeStamp'):]
                line = line.replace('\t','').replace('\n','')
                line = line.replace('timeStamp', 'timeStamp=') + '; '
                s += line
            elif line.find('token')!=-1:
                line = line[line.find('token'):]
                line = line.replace('\t','').replace('\n','')
                line = line.replace('token', 'token=') + '; '
                s += line
            elif line.find('uiapp')!=-1:
                line = line[line.find('uiapp'):]
                line = line.replace('\t','').replace('\n','')
                line = line.replace('uiapp', 'uiapp=') + '; '
                s += line
            elif line.find('userId')!=-1:
                line = line[line.find('userId'):]
                line = line.replace('\t','').replace('\n','')
                line = line.replace('userId', 'userId=') + '; '
                s += line
    print s
