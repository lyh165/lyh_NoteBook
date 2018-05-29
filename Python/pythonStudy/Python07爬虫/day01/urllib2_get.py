# coding=UTF-8
import urllib
import urllib2

url = "http://www.baidu.com/s"
headers = {"User-Agent":"Mozilla..."}

keyword = raw_input("请输入需要查询的字符串:")
wd = {"wd":keyword}
# print wd
# 通过urllib.urlencode()参数是一个dict类型
wd = urllib.urlencode(wd)
# print wd

# 拼接完整的url
fullurl = url + "?" +wd
print fullurl

# 构造一个请求
request = urllib2.Request(fullurl,headers = headers)

# 获取一个响应对象
response = urllib2.urlopen(request)
print  response.read()



#请输入需要查询的字符串:传智播客
#{'wd': '\xe4\xbc\xa0\xe6\x99\xba\xe6\x92\xad\xe5\xae\xa2'}
#wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2
#http://www.baidu.com/s?wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2

