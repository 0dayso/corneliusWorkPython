# coding:utf-8

import logging
import sys
import json

WEB = 60
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
VERBOSE = 5
NOTSET = 0


def addLevel():
    logging.addLevelName(WEB,'WEB')
    logging.addLevelName(logging.ERROR,'E')
    logging.addLevelName(logging.WARNING,'W')
    logging.addLevelName(logging.INFO,'I')
    logging.addLevelName(logging.DEBUG,'D')
    logging.addLevelName(VERBOSE,'V')

def basic():
    addLevel()
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        stream=sys.stdout)

def log(level,*args,**kwargs):
    logging.log(level,*args,**kwargs)

def web(*args, **kwargs):
    log(WEB,*args, **kwargs)
    sys.stdout.flush()

def v(*args, **kwargs):
    log(VERBOSE,*args, **kwargs)

def d(*args, **kwargs):
    log(DEBUG,*args, **kwargs)

def i(*args, **kwargs):
    log(INFO,*args, **kwargs)

def w(*args, **kwargs):
    log(WARN,*args, **kwargs)

def e(*args, **kwargs):
    log(ERROR,*args, **kwargs)

verbose = v
debug = d
info = i
warn = w
error = e


# 格式化输出,使用json.dumps简单实现
def fmt(s,level=INFO):
    logging.log(level,json.dumps(s, ensure_ascii=False, indent=2))

basic()




