# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanmovieSpider(scrapy.Spider):
	name = "doubanmovie"
	allowed_domains = ["movie.douban.com"]
	offset = 0
	url = 'https://movie.douban.com/top250?start='
	start_urls = (
		url+str(offset),
	)
	#print  start_urls

	def parse(self, response):
		pass

		print "===============" + response.url
		item = DoubanItem()
		# 根节点
		movies = response.xpath("//div[@class='info']")
		for each in movies:
			# ./ 是movies这个根节点
			# 
			item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
			item['bd'] = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
			item['star'] = each.xpath(".//div[@class='bd']//span[@class='rating_num']/text()").extract()[0]
			quote = each.xpath(".//p[@class='quote']/span/text()").extract()
			#print item['title']
			# 列表，如果有数据 就赋值 ，没有就跳过
			if len(quote) != 0:
				item['quote'] = quote[0]
# 将数据返回到管道进行处理
			yield item

		if self.offset < 225:
			self.offset += 25
# 一页的数据爬取完之后 ，重新去爬取下一页的内容
			yield scrapy.Request(self.url+str(self.offset),callback = self.parse)


					






