#coding=UTF-8

import urllib2

#urlopen 不支持代理访问 所以需要hander 处理器
# 为什么要使用代理访问,因为这是反爬虫的第二步，如果你请求一个链接多次,别人知道就会封ip
# 所以就需要代理访问



# 构建一个 HTTPHandler处理器对象，支持处理HTTP的请求
# 支持debug信息
# 在HTTPHandler增加参数 debuglevel=1 将会自动打开 Debug log 模式
# 程序在执行的时候 会打印收发包的信息
http_handler = urllib2.HTTPHandler(debuglevel=1)

# 调用build_opener()方法构建一个 自定义的opener对象，参数是构建的处理器对象
opener = urllib2.build_opener(http_handler)

request = urllib2.Request("http://www.baidu.com/")

response = opener.open(request)


# print response.read()