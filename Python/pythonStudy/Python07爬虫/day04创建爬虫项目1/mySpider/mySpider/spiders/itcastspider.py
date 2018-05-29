#coding=utf-8
# 爬虫的流程 url->调度器->下载器(得到响应文件)-> 回传到spider 
# spider 可以根据 继续爬取 或者 存数据到 item里面
import scrapy

# mySpider路径下的items模块 的 ItcastItem类
from mySpider.items import ItcastItem

# 创建一个爬虫类
class ItcastSpider(scrapy.Spider):
# 必要操作
	# 爬虫名	
	name = "itcast"
	# 允许爬虫作用的范围
	allowd_domains = ["http://www.itcast.cn/"]
	# 爬虫起始的url
	start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]
	
	def parse(self,response):
	#	with open("techer.html","w") as f:
	#		f.write(response.body)

	# 通过scrapy 自带的xpath匹配出所有老师的根节点列表集合
		techer_list = response.xpath('//div[@class="li_txt"]')
		# 所有老师信息的列表集合
		teacherItems = []
		# 遍历根节点集合
		for each in techer_list:
			# 实例化一个item 用来保存数据的
			item = ItcastItem() 
			# 将xpath对象 转换程unicode对象  extract()
			# extract() 将匹配出来的结果 转换程 Uniode字符串
			# 不加extract() 结果为xpath匹配对象
			name = each.xpath('./h3/text()').extract()
			title = each.xpath('./h4/text()').extract()
			info = each.xpath('./p/text()').extract()
			
			#print name[0]
			#print title[0]
			#print info[0]

			# 存储数据
			item['name'] = name[0]
			item['title'] = title[0]
			item['info'] = info[0]
			teacherItems.append(item)

		return teacherItems

			
