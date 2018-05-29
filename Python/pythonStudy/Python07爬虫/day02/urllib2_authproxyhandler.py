#coding=utf-8
import urllib2

# 爬虫一般使用多个ip。 通常会进行购买账号
# 如何使用带有账号的代理
# authproxy_handler = urllib2.ProxyHandler({"http":"授权账号:授权密码@ip:端口号"})
# 一般授权账号、密码是放到系统环境变量里面的
authproxy_handler = urllib2.ProxyHandler({"http":"60.247.121.230:3128"})


# 构建了一个全局的opener，之后所有的请求都可以用 urlopen()方式去发送,也附带handler功能
urllib2.install_opener(opener)
request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)
print response.read()
