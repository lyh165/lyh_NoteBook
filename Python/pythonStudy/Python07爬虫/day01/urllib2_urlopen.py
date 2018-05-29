# coding=UTF-8
#! /usr/bin/env python


import urllib2

# 向指定的url地址发送请求,并返回服务器响应的类文件对象
response = urllib2.urlopen("http://www.baidu.com/")

# 服务网器返回的类文件对象 支持python的操作方法
#read()方法就是读取文件的全部内容，返回字符串
html=response.read()
#打印响应内容
print html
