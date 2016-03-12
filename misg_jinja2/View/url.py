#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 引入相关模板
from jinja2 import Template
from wsgiref.simple_server import make_server

# 定义index页面处理函数
def index():
    # 读取index.html内容并返回值
    index_data = open('Templates/index.html','rb').read()
    return index_data
# 定义login页面处理函数
def login():
    # 读取login.html内容并返回值
    login_data = open('Templates/login.html','rb').read()
    #对login进行渲染
    template = Template(login_data)
    tmp = template.render(name='alan',age='25')
    #将渲染后的结果返回 注意一定要转码哦！！！
    return tmp.encode('utf8')

def route():
    #定义处理函数和页面映射 并返回映射关系
    r = [('/index/',index),('/login/',login),]
    return r

