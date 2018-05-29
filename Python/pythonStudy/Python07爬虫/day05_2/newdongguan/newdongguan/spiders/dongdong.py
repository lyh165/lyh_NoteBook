# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from newdongguan.items import NewdongguanItem


class DongdongSpider(CrawlSpider):
	
	name = 'dongdong'
	# 只能在此站点进行爬取数据
	allowed_domains = ['wz.sun0769.com']
	# 开始要爬取的页面
	start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
	# 每页的匹配规则
	pagelink = LinkExtractor(allow=("type=4"))
	# 每页里的每个帖子的匹配规则
	contentlink = LinkExtractor(allow=(r"/html/question/\d+/\d+.shtml"))

	"""
	Rule(LinkExtractor(allow=r'type=4'),process_links = "deal_links",follow = True),
    Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'),callback = "parse_item"),
	# 本案例的url被web服务器篡改，需要调用process_links来处理提取出来的url
		# 默认follow是true 可以不写
        #Rule(LinkExtractor(allow=r'type4'),process_links = "deal_links", follow=True),

		# 每个帖子 (callback不需要跟进 ,默认是None)
	"""
	rules = (
		Rule(pagelink,process_links = "deal_links"),
		Rule(contentlink,callback = "parse_item")
    )
	
	# links 是当前response 里 提取出来的链接列表
	def deal_links(self,links):
		for each in links:
			each.url =  each.url.replace("?","&").replace("Type&","Type?")
		return links

	def parse_item(self, response):
		print response.url
		item = NewdongguanItem()
		item['title'] = response.xpath('//div[contains(@class,"pagecenter p3")]//strong/text()').extract()[0]
		# 编号
		item['number'] = item['title'].split(' ')[-1].split(":")[-1]
		# 内容,先取出有图片的情况下匹配规则，如果有内容，返回所有内容的列表集合，如果没有内容
		content = response.xpath('//div[@class="contentext"]/text()').extract()
		#如果没有内容，则返回空列表，则无图片情况下的匹配规则
		if len(content)== 0:
			content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
			item['content'] = "".join(content).strip()
		else:
			item['content'] = "".join(content).strip()
		# 链接
		item['url'] = response.url
		yield item
