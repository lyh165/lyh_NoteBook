# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入mongoDB数据库
import pymongo
from scrapy.conf import settings

class DoubanPipeline(object):
	def __init__(self):
		# 获取settings文件里面的值
		host = settings["MONGODB_HOST"]
		port = settings["MONGODB_PORT"]
		dbname = settings["MONGODB_DBNAME"]
		sheetname = settings["MONGODB_SHEETNAME"]
		# 链接mongodb
        # 创建MONGODB数据库链接
		client = pymongo.MongoClient(host = host, port = port)
		# 指定数据库
		mydb = client[dbname]
		# 存放数据的数据库表名
		self.sheet = mydb[sheetname]
		#print "初始化管道"
		#print client

	def process_item(self, item, spider):

		data = dict(item)
		# 往表里面插入数据
		self.sheet.insert(data)
		return item
