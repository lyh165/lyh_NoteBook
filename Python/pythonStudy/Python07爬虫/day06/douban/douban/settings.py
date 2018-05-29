# -*- coding: utf-8 -*-

# Scrapy settings for douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

#USER_AGENT = "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"
#DOWNLOADER_MIDDLEWARES = {
#	'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#}
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douban.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# 下载中间件 用来处理请求之前的操作等等
# 请求之前的操作，一般是用于做反爬虫机制 反爬虫一般是 设置 useragent和使用多个代理ip进行访问 需要爬取的网页

#DOWNLOADER_MIDDLEWARES = {
#    'douban.middlewares.RandomUserAgent': 100,
#    'douban.middlewares.RandomProxy': 200,
#}
USER_AGENTS = [
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
	'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
	'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
	'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
	'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
	'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13', 
]

# 私密代理 可以设置多个代理 每个代理都是一个字典
# 包含 ip地址和端口号，帐号和密码
# 写法  {"ip_port":"121.42.140.113:16816","user_password":"mr_mao_hacker:sffary9r"}
PROXIES = [
	#{"ip_port":"121.42.140.113:16816","user_passwd":"mr_mao_hacker:sffary9r"}
	#{"ip_port":"115.223.238.121:9000","user_passwd":""}
	
	
]

#LOG_FILE = "douban.log"
#LOG_LEVEL = "DEBUG"


# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'douban.pipelines.DoubanPipeline': 300,
}
# MONGODB 主机名
MONGODB_HOST = "127.0.0.1"
# MONGODB 端口号
MONGODB_PORT = 27017
#数据库名称
MONGODB_DBNAME = "Douban"
# 存放数据的表名称
MONGODB_SHEETNAME = "doubanmovies"


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
