#coding=utf-8
import urllib2
# import time
# 高匿 别人只能拿到代理的ip 不能获取我们真正的ip
# 透明 别人能拿到代理ip 和 我们真正的ip
# 代理的国家 比如美国 就可以上facebook、谷歌


#代理开关，表示是否启用代理
proxyswith = False

# 构建一个handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
httpproxy_handler = urllib2.ProxyHandler({"http":"60.247.121.230:3128"})
# 构建了一个没有代理的处理器对象
nullproxy_handler = urllib2.ProxyHandler({})

if proxyswith:
	opener = urllib2.build_opener(httpproxy_handler)
else:
	opener = urllib2.build_opener(nullproxy_handler)

# 构建了一个全局的opener，之后所有的请求都可以用 urlopen()方式去发送,也附带handler功能
urllib2.install_opener(opener)
# time.sleep(1)	
request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)
print response.read()
# print response.read().decode("gbk")
