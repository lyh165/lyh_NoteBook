#coding=utf8

import urllib
import urllib2
import cookielib

#CookieJar()类构建一个cookieJar()对象，用来保持cookie的值

cookie = cookielib.CookieJar()

# 通过HTTPCookieProcessor() 处理器类构建一个处理器对象,用来处理cookie
# 参数就是构建的CookieJar()对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 构建一个自定义的opener 并且绑定了cookie的处理器
opener = urllib2.build_opener(cookie_handler)

# 通过自定义opener的addheader的参数，可以添加HTTP报头参数
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")] 


# 人人网的登陆接口 每次访问都是同一个cookie
url = "http://www.renren.com/PLogin.do"
# SysHome.do 访问会出错
# url = "http://www.renren.com/SysHome.do"


# 需要登陆的账号密码
data = {"email":"liyuhong165@163.com","password":"lyh5992858."}
# 通过urlencode编码转码
data = urllib.urlencode(data)

# 第一次是post请求，生成登录后的cookie (如果登录成功的话)
request = urllib2.Request(url,data = data)
# 发送第一次的post请求
response = opener.open(request)
#print response.read()


# 第二次可以是get请求，这个请求保存生成cookie一并发到web服务器，服务器会验证cookie通过
respsonse_zhou = opener.open("http://www.renren.com/224452292/profile")
# 获取登录后才能访问的页面信息
print respsonse_zhou.read()