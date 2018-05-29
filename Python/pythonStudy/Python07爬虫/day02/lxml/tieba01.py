#!C:\Python27\python
# -*- coding: utf-8 -*-
# 
import urllib
import urllib2
from lxml import etree


def loadPage(url):
	"""
	作用:根据url发送请求,获取服务器响应文件
	url:需要爬去的url地址
	"""
	# print url
	# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
	request = urllib2.Request(url)
	html = urllib2.urlopen(request).read()
	# print html
	# 解析HTML文档为 HTML DOM模型
	content = etree.HTML(html)
	# 返回所有匹配成功的列表集合
	link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
	for link in link_list:
		fulllink = "http://tieba.baidu.com" + link
		# 组合每个帖子的链接
		#print fulllink
		loadImage(fulllink)

# 取出每个帖子里的每个图片链接
def loadImage(link):
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
	request = urllib2.Request(link, headers = headers)
	html = urllib2.urlopen(request).read()
	#解析	
	content = etree.HTML(html)
	# 取出帖子厘每层层主发送的图片链接集合
	link_list = content.xpath('//img[@class="BDE_Image"]/@src')
	# 取出每个图片的链接
	for link in link_list:
		#print link
		writeImage(link)


def writeImage(link):
	"""
	作用：将html内容写入到本地
	link:图片链接
	"""	
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
	# print "正在保存" + filename
	request = urllib2.Request(link,headers = headers)
	# 图片原始数据
	image = urllib2.urlopen(request).read()
	# 取出链接后10位作为文件名
	filename = link[-10:]
	# 写入刀本地磁盘文件内 (二进制存入)
	with open(filename,'wb') as f:
		f.write(image)
	print "已经成功下载" + filename

def tiebaSpider(url,beginPage,endPage):
	# 最终查询出来的url是 	#https://tieba.baidu.com/f?kw=%E4%BC%A0%E6%99%BA%E5%8D%9A%E5%AE%A2&pn=100

	"""
	作用：贴吧爬虫调度器，负责组合处理每个页面的url
	url: 贴吧url的前部分
	beginPage: 起始页
	endPage: 结束页
	"""
	for page in range(beginPage,endPage+1): # 爬去1-6 那么 这里是5页 我们需要爬去6页
		pn = (page -1) *50
		#filename = "第" + str(page) + "页.html"
		# 拼接
		fullurl = url + "&pn=" + str(pn)
		# print fullurl
		# html = loodPage(fullurl,filename)
		# print html
		loadPage(fullurl)
	print "谢谢使用"


if __name__ == "__main__":
	kw = raw_input("请输入需要爬去的贴吧名:")
	beginPage = int(raw_input("请输入起始页:"))
	endPage = int(raw_input("请输入结束页:")) 
	url = "https://tieba.baidu.com/f?"
	#https://tieba.baidu.com/f?kw=%E4%BC%A0%E6%99%BA%E5%8D%9A%E5%AE%A2&pn=100
	key = urllib.urlencode({"kw":kw})
	fullurl = url + key 
	tiebaSpider(fullurl,beginPage,endPage)

