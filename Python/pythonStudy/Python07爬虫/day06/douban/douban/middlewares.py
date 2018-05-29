#coding=utf-8
import random
# base64用来加密处理
import base64

from settings import USER_AGENTS
from settings import PROXIES

#该文件是用来进行反爬虫机制而指定的，反爬虫一般会根据user-agent和ip地址。
# 所以我们需要指定一套 user-agent 和 代理ip 进行帮我们模拟用户访问。从而达到爬虫效果

# 随机的User-Agent
class RandomUserAgent(object):
	def process_request(self,request,spider):
		useragent = random.choice(USER_AGENTS)
		#print useragent
		# 设置一个默认的请求报文头
		request.headers.setdefault("User-Agent",useragent)
		#print request.headers.setdefault("User-Agent",useragent)

# 随机 代理
# 代理分为 有帐号、和 无帐号

class RandomProxy(object):
	def process_request(self,request,spider):
		proxy = random.choice(PROXIES)
		print proxy
		print proxy['user_passwd']
		# 保存代理 有帐号的代理 和 保存无帐号的代理ip
		#if proxy['user_passwd'] is None:		
		if proxy['user_passwd'] is "":
			# 没有代理账户验证的代理使用方法
			print "111"
			print proxy['ip_port']
			request.meta['proxy'] = "http://" + proxy['ip_port']
			print request.meta['proxy']

			
		else:
			print "222"
			# 先获取ip和端口号 
			# request.meta['proxy'] = "http://" + proxy['ip_port']
			request.meta['proxy'] = "http://" + proxy['ip_port']
			
			# 有帐号验证的代理，需要通过base64转换
			base64_userpasswd = base64.b64encode(proxy['user_passwd'])
			print base64_userpasswd
			# 对应刀代理服务器的信令格式里
			request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd

			
