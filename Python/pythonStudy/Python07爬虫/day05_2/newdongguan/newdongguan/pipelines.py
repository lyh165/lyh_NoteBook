# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json 

# 写入文件的时候 不需要每次都写入utf-8. 直接在编写文件设置文本的格式是utf-8即可
import codecs


class NewdongguanPipeline(object):
	def __init__(self):
		# 创建一个文件
		self.filename = codecs.open("dongguan.json","w",encoding="utf-8")

	def process_item(self, item, spider):
		# 中文默认使用ascii码来存储， 禁用后 默认为uncode字符串
		#
		content = json.dumps(dict(item), ensure_ascii = False) + ",\n"
		#self.filename.write(text.encode("utf-8"))
		self.filename.write(content)
		return item

	def close_spider(self,spider):
		self.filename.close()
		
