#coding=utf-8

import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs 
# as 是起别名


class douyu(unittest.TestCase):
	# 初始化方法
	def setUp(self):
		# 需要设置环境变量 可以在 /etc/profile里面设置 
		self.dirver = webdriver.PhantomJS()
		# /usr/local/phantomjs/bin

		#chromedriver = '/usr/local/bin/chromedriver'
		#os.environ["webdriver.chrome.driver"] = chromedriver
		#browser = webdriver.Chrome(chromedriver)
		#self.dirver = webdriver.PhantomJS(executable_path="/usr/local/phantomjs/bin/.phantomjs")
		
		self.num = 0 
		self.count = 0
	# 测试方法必须有test字样开头
	def testDouyu(self):
		self.dirver.get("https://www.douyu.com/directory/game/LOL")
		while True:
			soup = bs(self.dirver.page_source,"lxml")
			# 房间名 返回列表
			names = soup.find_all("h3",{"class":"ellipsis"})
			# 观看人数 返回列表
			numbers = soup.find_all("span",{"class":"dy-num fr"})
			# zip(names,numbers) 将name 和 number 这两个列表合并为一个元组[(1,2) (3,4)]...
			for name,number in zip(names,numbers):
				print u",观众人数: " + number.get_text().strip() + u"\t房间名: " + name.get_text().strip() 
				self.num +=1
				# self.count +=int(number.get_text().strip())
			# 如果在页面源码里面 找到“下一页”为隐藏的标签，就退出循环
			if self.dirver.page_source.find("shark-pager-disable-next") != -1:
				break				
			# 点击事件
			self.dirver.find_element_by_class_name("shark-pager-next").click()
				
	# 测试结束执行的方法
	def tearDown(self):
		# 退出PhantomJS()浏览器
		print self.num
		#print self.num
		self.dirver.quit()

if __name__ == '__main__':
	#启动测试模块
	unittest.main()

# https://www.douyu.com/directory/game/LOL

# 姓名
# h3 class="ellipsis"
# 观看人数
# span class="dy-num fr"
# 下一页
# class="shark-pager-item current"
# 下一页不可以点
# class="shark-pager-next shark-pager-disable shark-pager-disable-next"
