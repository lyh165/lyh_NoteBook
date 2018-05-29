# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
	name = "tencent"
	allowed_domains = ["tencent.com"]
	# https://hr.tencent.com/position.php?&start=10#a
	url = "https://hr.tencent.com/position.php?&start="    
	offset = 0
	start_urls = [url + str(offset)]
	print "链接是" + str(start_urls)
	def parse(self,response):
# for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
		for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
			# 初始化模型对象
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
	

		if self.offset <1680:
			self.offset +=10
				#else:
				#	raise "结束工作"
		# 每次处理一页数据之后 重新发送下一页页面请求	
		# self.offset自增10，同时拼接为新的url,并调用回调函数 self.parse处理Response
		yield scrapy.Request(self.url + str(self.offset),callback = self.parse)



