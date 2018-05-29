# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os 

class ImagePipeline(ImagesPipeline):
    #def process_item(self, item, spider):
     #   return item
	# 获取settings文件设置的变量值
	
	# 图片的目录
	IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

	def get_media_requests(self,item,info):
		image_url = item["imagelink"]
		yield scrapy.Request(image_url)

	def item_completed(self,result,item,info):
		# 图片的哈希值
		image_path =[x["path"] for ok, x in result if ok]
		# 通过图片的哈希值，修改成我们自己的名字
		os.rename(self.IMAGES_STORE + "/" + image_path[0],self.IMAGES_STORE + "/" + item["nickname"] + ".jpg")
		# 图片的路径		
		item["imagePath"] = self.IMAGES_STORE + "/" + item["nickname"]
		return item
	
