# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


import scrapy

class ItcastItem(scrapy.Item):
	# 姓名、职称、个人简介
	name = scrapy.Field()
	title = scrapy.Field()	
	info = scrapy.Field()
