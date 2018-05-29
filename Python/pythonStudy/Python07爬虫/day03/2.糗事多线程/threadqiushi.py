#coding=utf-8

# 使用现场库
import threading
# 队列
from Queue import Queue
# 解析库
from lxml import etree
#请求处理
import requests
#json处理
import json
import time 

# 采集类
class ThreadCrawl(threading.Thread):
	def __init__(self,threadName,pageQueue,dataQueue):
		#threading.Thread.__init__(self)
		# 调用父类的初始化方法
		super(ThreadCrawl,self).__init__()
		#线程名
		self.threadName = threadName
		# 页码队列
		self.pageQueue = pageQueue
		# 数据队列
		self.dataQueue = dataQueue
		# 请求报头
		self.headers = {
			        "User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
		}
	def run(self):
		print "启动" + self.threadName
		while not CRAWL_EXIT:
			try:
				# 取出一个数字，先进先出
				# 可选参数 block, 默认为True
				# 1.如果队列为空，block为True的话，就会进入阻塞状态，直到队列有新的数据
				# 2.如果队列为空，block为False的话，就弹出一个Queue.empty()异常
				page = self.pageQueue.get(False)
				# https://www.qiushibaike.com/8hr/page/1/
				url = "https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
				#print url 
				time.sleep(1)
				content = requests.get(url,headers = self.headers).text
				#print content
				self.dataQueue.put(content)
				#print len(content)
			except:
				pass
		print "结束" + self.threadName

# 解析类
class ThreadParse(threading.Thread):
	def __init__(self,threadName,dataQueue,filename,lock):
		super(ThreadParse,self).__init__()
		# 线程名
		self.threadName = threadName
		# 数据队列
		self.dataQueue = dataQueue
		# 保存解析后数据的文件名
		self.filename = filename
		# 锁
		self.lock = lock

	def run(self):
		print "启动" + self.threadName
		while not PARSE_EXIT:
			try:
				# print self.dataQueue
				html = self.dataQueue.get(False)
				self.parse(html)

			except:
				pass
		print "结束" + self.threadName

	def parse(self,html):
		html = etree.HTML(html)
		# 返回所有段子的结点位置，contains()模糊查询方法 第一个参数是匹配的标签，第二个参数是标签名部分内容
		node_list = html.xpath('//div[contains(@id,"qiushi_tag")]')

		#print node_list 
		for node in node_list:
			#xpath返回的是一个列表，这个列表就一个参数，用索引方式取出来，用户名
			# 用户名
			username = node.xpath('.//h2')[0].text
			#图片链接
			image = node.xpath('.//div[@class="thumb"]//@src')#[0]
			# 段子内容
			content = node.xpath('.//div[@class="content"]/span')[0].text
			# 点赞
			zan = node.xpath('.//i')[0].text
			#评论
			comments = node.xpath('.//i')[1].text
			
			items = {
				"username" : username,
				"image":image,
				"content":content,
				"zan":zan,
				"comments":comments
			}

			# with 后面有两个必须执行的操作：__enter__ 和 _exit__
            # 不管里面的操作结果如何，都会执行打开、关闭
            # 打开锁、处理内容、释放锁
			with self.lock:
				# 写入存储的解析后的数据
				self.filename.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")



CRAWL_EXIT = False
PARSE_EXIT = False

def main():
	# 页码的队列，表示10个页面
	pageQueue = Queue(10)
	# 放入1~10的数字，先进先出
	for i in range(1,11):
		pageQueue.put(i)


	# 采集结果(每页的HTML源码)的数据队列，参数为空 表示无限制
	dataQueue = Queue()

	filename = open("duanzi.json","a")
	 # 创建锁
	lock = threading.Lock()

	# 是哪个采集线程的名字
	crawList = ["采集线程1号","采集线程2号","采集线程3号",]

	# 存储是是三个采集线程
	Threadcrawl = []
	for threadName in crawList:
		thread = ThreadCrawl(threadName,pageQueue,dataQueue)
		thread.start()
		Threadcrawl.append(thread)

	#三个解析线程的名字
	parseList = ["解析线程1号","解析线程2号","解析线程3号"]
	# 存储三个解析线程
	threadparse = []

	for threadName in parseList:
		 thread = ThreadParse(threadName,dataQueue,filename,lock)
		 thread.start()
		 threadparse.append(thread)


	# 等待pageQueue队列为空,也就是等待之前的操作执行完毕
	while  not pageQueue.empty():
		pass
	# 如果pageQueue为空 采集线程退出循环	
	global CRAWL_EXIT
	CRAWL_EXIT = True
	print "pageQueue采集为空"
	# 阻塞 等待子线程采集完毕 才执行父线程
	for thread in Threadcrawl:
		thread.join()
		print "1"
	


	# 解析数据
	while not dataQueue.empty():
		pass

	global PARSE_EXIT
	PARSE_EXIT = True

	for thread in threadparse:
		thread.join()
		print "2"

	with lock:
		# 关闭文件
		filename.close()
	print "谢谢使用！"





if __name__ == '__main__':
	main()
