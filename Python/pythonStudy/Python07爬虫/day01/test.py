import urllib2

# 可以是User-Agent列表，也可以是代理列表
headers = {"User-Agent":"Mozilla/5.0(Win"}
request = urllib2.Request("http://www.baidu.com/",headers = headers)
response = urllib2.urlopen(request)

# print response.read()

# 返回http的响应码,成功返回200. 4服务器页面出错，403重定向 5服务器问题
print response.getcode()

# 返回 返回实际数据的实际URL，防止重定向问题
print response.geturl()

# 返回服务器响应的HTTP报头
print response.info()

# GET http://www.baidu.com/ HTTP/1.1
# Accept-Encoding: identity
# Host: www.baidu.com
# Connection: close
# User-Agent: Python-urllib/2.7
