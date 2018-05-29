# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
	# 标题、信息、评分、简介
	title = scrapy.Field()
	bd = scrapy.Field()
	star = scrapy.Field()
	quote = scrapy.Field()
