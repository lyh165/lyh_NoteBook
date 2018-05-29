# coding=UTF-8
#! /usr/bin/env python


import urllib2


# 爬虫和反爬虫的斗争 第一部
ua_headesr = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
#通过urllib2.request()方法构造一个请求对象
request = urllib2.Request("http://www.baidu.com/",headers = ua_headesr)


# 向指定的url地址发送请求,并返回服务器响应的类文件对象
response = urllib2.urlopen(request)

# 服务网器返回的类文件对象 支持python的操作方法
#read()方法就是读取文件的全部内容，返回字符串
html=response.read()

# 返回http的响应码,成功返回200. 4服务器页面出错，403重定向 5服务器问题
print response.getcode()

# 返回 返回实际数据的实际URL，防止重定向问题
print response.geturl()

# 返回服务器响应的HTTP报头
print response.info()

#打印响应内容
#print html






#GET https://www.baidu.com/ HTTP/1.1
#Host: www.baidu.com 域名
#Connection: keep-alive 保存长链接 爬虫获取一个
#Upgrade-Insecure-Requests: 1 
#User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36 必写  
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8 获取什么样的数据 json 页面 默认可以不写
#Accept-Encoding: gzip, deflate, br 是否可以处理压缩 一定不能写
#Accept-Language: zh-CN,zh;q=0.9 语言 不需要写
#Cookie: 222

