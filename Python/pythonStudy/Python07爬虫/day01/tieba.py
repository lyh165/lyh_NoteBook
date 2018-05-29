#!C:\Python27\python
# -*- coding: utf-8 -*-
# 
import urllib
import urllib2

def loodPage(url,filename):
	"""
	作用:根据url发送请求,获取服务器响应文件
	url:需要爬去的url地址
	filename: 处理的文件名
	"""
	print "正在下载" + filename
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
	request = urllib2.Request(url, headers = headers)
	return urllib2.urlopen(request).read()


def writePage(html,filename):
	"""
	作用：将html内容写入到本地
	html: 服务器响应文件内容
	"""	
	print "正在保存" + filename

	# 文件写入
	with open(filename,'w') as f:
		f.write(html)
	print "-" * 30

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
		filename = "第" + str(page) + "页.html"
		# 拼接
		fullurl = url + "&pn=" + str(pn)
		# print fullurl
		html = loodPage(fullurl,filename)
		# print html
		writePage(html,filename)
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

