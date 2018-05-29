# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dongguan.items import DongguanItem


class SunSpider(CrawlSpider):
	"""
	能访问 http://wz.sun0769.com/index.php/question/questionType?page=30&type=4
	反爬虫 http://wz.sun0769.com/index.php/question/questionType&type=4?page=90900
	主要区别在于 
	http://wz.sun0769.com/index.php/question/questionType	?page=30&type=4
	http://wz.sun0769.com/index.php/question/questionType	&type=4?page=90900
	"""

	name = 'sun'
	allowed_domains = ['wz.sun0769.com']
	start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

	rules = (
		Rule(LinkExtractor(allow=r'type=4'),process_links = "deal_links",follow = True),
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'),callback = "parse_item"),
	)

	

	# 需要重新处理每个response厘提取的链接，type&page=xxx?type=4 修改为Type?page=xxx&type4
	def deal_links(self,links):
		# 迭代器		
		for link in links:
			#re.sub(s1,s2,string)
			# 把所有的? 改成 &
			link.url = link.url.replace("?","&").replace("Type&","Type?")
			#print link.url
		# 返回修改完的links链接列表
		return links
		
	def parse_item(self, response):
		print response.url

		item = DongguanItem()
		item['title'] = response.xpath('//div[contains(@class,"pagecenter p3")]//strong/text()').extract()[0]
		# 编号
		item['number'] = item['title'].split(' ')[-1].split(":")[-1]
		# 内容
		item['content'] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
		# 链接
		item['url'] = response.url


		yield item


