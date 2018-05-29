# coding=UTF-8
import urllib
import urllib2
import ssl


# 如果没有安装ssl数字认证证书(ssl认证是通过数字认证的) 访问百度的https 会跳到重定向
#url = "https://www.baidu.com/"
#request = urllib2.Request(url)
#repsonse = urllib2.urlopen(request)
#print repsonse.read()



# 忽略SSL安全认证
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# ssl.CertificateError:
url = "https://www.12306.cn/mormhweb/"
context = ssl._create_unverified_context()
request = urllib2.Request(url, headers = headers)
# 3. 在urlopen()方法里 指明添加 context 参数
response = urllib2.urlopen(request, context=context)
print response.read()
