# coding=UTF-8
import urllib
import urllib2
import json 

# url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule" 通过fidder抓取过来的解开 错误 .需要去除 _o
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# 用户输入
key = raw_input("请输入需要翻译的文字:")
headers = {
			#"Accept":"application/json, text/javascript, */*; q=0.01",
			"X-Requested-With":"XMLHttpRequest",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
			"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
}


# 发送到web服务器的表单数据
fromdata = {
"i":key,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":"1526487798490",
"sign":"4e7f2a468ef9dcb71d4782d07d3153c1",
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_CLICKBUTTION",
"typoResult":"false"
}

# 经过urlencode转码
data = urllib.urlencode(fromdata)

# 如果request里面方法的data有值，那么这个请求就是post请求
# 如果没有就是get
request = urllib2.Request(url,data=data,headers = headers)
response = urllib2.urlopen(request)
print response.read()

#html = response.read().decode('utf-8')
#target = json.loads(html)
#print("result: %s" % (target['translateResult'][0][0]['tgt']))





"""
i=python
from=AUTO
to=AUTO
smartresult=dict
client=fanyideskweb
salt=1526487798490
sign=4e7f2a468ef9dcb71d4782d07d3153c1
doctype=json&version=2.1
keyfrom=fanyi.web
action=FY_BY_CLICKBUTTION
typoResult=false
"""
