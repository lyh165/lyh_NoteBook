#coding=utf-8
import urllib2
# json 解析库 对应到lxml
import json
# json的解析语法 对应到xpath
import jsonpath

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
# 去除json文件里的内容，返回的格式是字符串
html = response.read()

#把json形式的字符串转换成 python字形式的 unicode字符串
unicodeer = json.loads(html)

# python形式的列表
city_list = jsonpath.jsonpath(unicodeer,"$..name")
for item in city_list:
	print item



#返回的是unicode格式
array = json.dumps(city_list,ensure_ascii=False)

with open("lagoucity.json",'w') as f:
	f.write(array.encode("utf-8"))

