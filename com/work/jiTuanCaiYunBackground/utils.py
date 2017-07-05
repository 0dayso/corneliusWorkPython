# coding=utf8

import random
import string
import json

def randint(length,firstZero=True):
    s = ''

    if firstZero :
        for i in range(length):
            s = s + random.choice(string.digits)
    else:
        s = s + random.choice('123456789')
        for i in range(length - 1):
            s = s + random.choice(string.digits)
    return s

def randchar(length):
    s = ''
    for i in range(length):
        s = s + random.choice(string.ascii_letters)
    return s

def randzh(length):
    """生成中文"""
    s = ''
    for i in range(length):
        s += Unicode()
    return s

def Unicode():
    val = random.randint(0x4E00, 0x9FBF)
    return unichr(val).encode('utf-8')



def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

def jsonLoadsUTF8(s):
    r = json.loads(s)
    if isinstance(r, list):
        r = _decode_list(r)
    elif isinstance(r, dict):
        r = _decode_dict(r)
    return r