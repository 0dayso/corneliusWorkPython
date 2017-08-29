#! usr/bin/python
# coding:UTF-8

import httplib
import json
import time
import login
import utils

import sys
sys.path.append('..')

from basic import config_file


def dealCookie():
    fileName = 'E:\\workspace\\corneliusWorkPython\\com\\work\\jtcyBackground\\core\\cookie.txt'
    s = ""
    f = open(fileName, "r")
    lines = f.readlines()
    for line in lines:
        if line[0] != '#':
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
                line = line.replace('uiapp', 'userInfo')
                s += line
            elif line.find('userId')!=-1:
                line = line[line.find('userId'):]
                line = line.replace('\t','').replace('\n','')
                line = line.replace('userId', 'userId=')
                s += line
    return s

class HttpResp:
    pass

def http(args):
    """
    args : {
        'url' : 'entadmin/contact/dept/save',
        'data' : {
        },
        'headers' : {
        },
        'cookie' : {
        }
    }
    """

    try:
        if config_file.IS_ON_LINE:
            host = config_file.SERVER_HOST_ON_LINE
            port = config_file.SERVER_PORT_ON_LINE
        else:
            host = config_file.SERVER_HOST
            port = config_file.SERVER_PORT

        # URL
        url = args['url']
        if config_file.IS_ON_LINE:
            if "https://admin.jituancaiyun.com/".find(url) != -1:
                if url[0] != '/':
                    url = '/' + url
        else:
            if "http://admin.jituancaiyun.net/".find(url) != -1:
                if url[0] != '/':
                    url = '/' + url
        # headers
        headers = {}
        if args.has_key('headers'):
            headers = args['headers']
            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            if config_file.IS_ON_LINE:
                headers['Host'] = 'admin.jituancaiyun.com'
            else:
                headers['Host'] = 'admin.jituancaiyun.net'
            headers['Accept-Encoding'] = 'gzip, deflate, sdch'
            headers['Accept-Language'] = 'zh-CN,zh;q=0.8,ja;q=0.6'
            headers['Content-Type'] = 'application/json;charset=UTF-8'
            headers['Cookie'] =  dealCookie()
            if config_file.IS_ON_LINE:
                headers['Referer'] = 'https://admin.jituancaiyun.com/'
            else:
                headers['Referer'] = 'http://admin.jituancaiyun.net/'
        else:
            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            if config_file.IS_ON_LINE:
                headers['Host'] = 'admin.jituancaiyun.com'
            else:
                headers['Host'] = 'admin.jituancaiyun.net'
            headers['Accept-Encoding'] = 'gzip, deflate, sdch'
            headers['Accept-Language'] = 'zh-CN,zh;q=0.8,ja;q=0.6'
            headers['Content-Type'] = 'application/json;charset=UTF-8'
            headers['Cookie'] = dealCookie()
            if config_file.IS_ON_LINE:
                headers['Referer'] = 'https://admin.jituancaiyun.com/'
            else:
                headers['Referer'] = 'http://admin.jituancaiyun.net/'


        # method 先取method的值，如果为空，则根据data进行判断，有数据就为POST
        method = args.get('method', args.has_key('data') and 'POST' or 'GET')

        # data
        data = args.has_key('data') and json.dumps(args['data']) or None

        startTime = time.time()
        response = _send(host, port, method, url, data, headers)
        endTime = time.time()

        body = response.read()
        jBody = None
        if len(body) > 0 and response.status == 200:
            try:
                # 默认转出来的字符串是unicode,转成utf8方便使用
                jBody = utils.jsonLoadsUTF8(body)
            except:
                pass
        # if not jBody['success'] and jBody['msg'] == '登录超时,请退出重新登录':
        #     login.login()
        #     http(args)

        resp = HttpResp()
        resp.time = endTime - startTime
        resp.code = response.status
        resp.msg = response.reason
        resp.headers = response.getheaders()
        resp.body = body
        resp.jBody = jBody
        return resp
    finally:
        pass

def _send(host, port, method, url, data, headers):
    http_client = httplib.HTTPConnection(host, port, timeout=30)
    http_client.request(method, url, data, headers)
    return http_client.getresponse()






