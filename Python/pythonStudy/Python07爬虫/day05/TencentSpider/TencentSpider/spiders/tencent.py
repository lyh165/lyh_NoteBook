# -*- coding: utf-8 -*-

import scrapy
# 导入crawlSpider类 和 rule
from scrapy.spiders import CrawlSpider,Rule
# 导入链接规则匹配类，用来提取符合规则的链接
from scrapy.linkextractors import LinkExtractor
from TencentSpider.items import TencentItem

class TencentSpider(CrawlSpider):
	name = "tencent"
	allow_domains = ["hr.tencent.com"]
	#start_url = ["https://hr.tencent.com/position.php?&start=0#a"]
	start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]
	#Response厘链接的提取规则，返回的符合匹配规则的链接 匹配对象的列表
	pagelink = LinkExtractor(allow=("start=\d+"))
	#newlink = LinkExtractor(allow=("e123123")) # 匹配多个链接
	rules = [
		# 获取这个列表厘的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
		Rule(pagelink,callback = "parseTencent",follow = True)
		#Rule(newlink,callback)
	]
	
	# 调用指定函数
	def parseTencent(self,response):
		#evenlist = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
		#oddlist = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
		#fulllist = evenlist + oddlist
		for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
			item = TencentItem()
			# 返回的是一个选择器的列表
			# 职位名
			item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
			# 详细链接
			item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]
			# 职位类型
			item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
			# 招聘人数
			item['peopleNum']	= each.xpath("./td[3]/text()").extract()[0]
			# 工作地点
			item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
			# 发布时间
			item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

			yield item
			


