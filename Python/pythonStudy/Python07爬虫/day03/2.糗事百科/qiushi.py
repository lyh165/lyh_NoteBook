#coding=utf-8
import urllib2
import json
from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/1/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

request = urllib2.Request(url,headers = headers)

html = urllib2.urlopen(request).read()

# 响应返回的是字符串， 解析成html dom格式模式
text = etree.HTML(html)

# 返回所有段子的结点位置，contains()模糊查询方法 第一个参数是匹配的标签，第二个参数是标签名部分内容
node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')
#print node_list 
for node in node_list:
	#xpath返回的是一个列表，这个列表就一个参数，用索引方式取出来，用户名
	# 用户名
	username = node.xpath('.//h2')[0].text
	#图片链接
	image = node.xpath('.//div[@class="thumb"]//@src')#[0]
	# 段子内容
	content = node.xpath('.//div[@class="content"]/span')[0].text
	# 点赞
	zan = node.xpath('.//i')[0].text
	#评论
	comments = node.xpath('.//i')[1].text
	
	items = {
		"username" : username,
		"image":image,
		"content":content,
		"zan":zan,
		"comments":comments
	}

	with open("qiushi.json","a") as f:
		f.write(json.dumps(items,ensure_ascii=False).encode("utf-8") + "\n")
