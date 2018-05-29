#coding=UTF-8
import urllib2
import random

url = "http://www.baidu.com/"

# 可以是User-Agent列表，也可以是代理列表
ua_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
		]

# 在User-Agent列表随机选择一个User-Agent
user_agent = random.choice(ua_list)	

#构造一个请求
request = urllib2.Request(url)	
response = urllib2.urlopen(request)

# add_header()方法 添加/修改 一个http报头
request.add_header("User-Agent",user_agent)

#get_header() 获取一个已有的HTTP报头的值，注意只能是第一个字母大写，其他的必须小写
print request.get_header("User-agent")

# print response.getcode()

# # 返回 返回实际数据的实际URL，防止重定向问题
# print response.geturl()

# # 返回服务器响应的HTTP报头
# print response.info()


