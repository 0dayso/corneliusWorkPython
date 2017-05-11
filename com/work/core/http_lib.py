# coding=utf8

# import httplib
import httplib
import urllib2
import json

from com.work.util import utils
from com.bjj.util import logger as log


class HttpResp:
    pass


def http(args):
    """
        args : {
            'url':'/medical/doctors/login',
            'data':{
            },
            'header':{
            },
            'Cookie':{
            },
            'token':True,
        }
    """


    try:
        # URL
        url = args['url']

        # TODO:有可以不是json
        data = args.has_key('data') and json.dumps(args['data']) or None

        # 发送请求
        response = _send(url, data)

        body = response.read()

        log.d('响应')


        return body

    finally:
        pass


def _send(url, data=None):
    request = urllib2.Request(url,data)
    response = urllib2.urlopen(request)
    return response

def http1(args, host, port):
    """
        args : {
            'url':'/medical/doctors/login',
            'data':{
            },
            'header':{
            },
            'Cookie':{

            },
            'token':True,
            'doctor':None
        }
    """


    try:

        # host = config.SERVER_HOST
        # port = 443

        # URL
        url = args['url']
        if url[0] != '/': url = '/' + url

        # header
        header = args.get('header', {})

        # 先取method的值，如果为空，则根据data进行判断，有数据就为POST
        method = args.get('method', args.has_key('data') and 'POST' or 'GET')

        # TODO:有可以不是json
        data = args.has_key('data') and json.dumps(args['data']) or None

        # 发送请求
        response = _send1(host, port, method, url, data, header)

        body = response.read()
        jbody = None

        if len(body) > 0 and response.status == 200:
            try:
                # 默认转出来的字符串是unicode,转成utf8方便使用
                jbody = utils.jsonLoadsUTF8(body)
            except:
                pass
        resp = HttpResp()
        resp.code = response.status
        resp.msg = response.reason
        resp.headers = response.getheaders()  # 获取头信息
        resp.body = body
        resp.jbody = jbody

        log.d('响应')
        log.v('    HEAD : %s', resp.headers)
        if len(body) > 1024:
            log.d('    BODYLEN: %d', len(body))
        else:
            if resp.body: log.d('    BODY   : %s', resp.body)
        return resp

    finally:
        pass

def _send1(host, port, method, url, data, header):
    http_client = httplib.HTTPConnection(host, port, timeout=30)
    http_client.request(method, url, data, header)
    return http_client.getresponse()

