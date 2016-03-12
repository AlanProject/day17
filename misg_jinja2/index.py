#!/usr/bin/env python
#-*- coding:utf-8 -*-
from View import url
#msgi 处理函数
def RunServer(eviron,start_response):
    # HTTP响应头部信息
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 用户请求信息
    data = eviron['PATH_INFO']
    # 获取对应关系
    r = url.route()
    # 定义一个常量
    func = None
    #循环对应关系
    for k in r:
        # 请求的URL是否和对应关系中的某一个匹配 如果匹配则赋值给func并退出循环
        if k[0] == data:
            func = k[1]
            break
    # 如果匹配到url 则执行对应的处理函数并返回结果
    if func:
        return func()
    # 如果未匹配到url则返回404
    else:
        return '404 is not found'
if __name__ == '__main__':
    # 配置msgi
    http = url.make_server('127.0.0.1',8001,RunServer)
    # 打印启动消息
    print 'Http server is start ok !'
    # 启动监听
    http.serve_forever()
