1.安装
	pip2 install scrapy 
	sudo apt install python-scrapy

2.创建项目 
	scrapy startproject 项目名称(mySpider)

(ie9请求报文头 : "User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;")
(中间件 比如 1～3 之间做的事情 1做完 我突然插进来 在3前面 而我就是中间件)
3.目录结构
		.
	├── mySpider	
	│   ├── __init__.py
	│   ├── items.py	存放数据
	│   ├── pipelines.py 管道文件 (数据交给管道，管道可以存在本地或者数据库)
	│   ├── settings.py	 核心文件 (爬虫存放的位置，是否支持robots协议，并发量 默认16 ，加载延迟 默认3秒，是否启动cookie(一般登录才会使用到cookie) 浏览其他页面不留痕迹，请求报头，爬虫的处理中间件，下载中间件，管道文件(下载好的数据怎么处理)
	│   └── spiders
	│       └── __init__.py
	└── scrapy.cfg		配置文件

4.创建一个爬虫模板
	scrapy genspider myspider(爬虫文件名) itcast.cn(需要爬取那个网站)

5.编辑代码(item类、爬虫类)

6.执行一个爬虫
	scrapy crawl itcast

7.导出一个json文件
	scrapy crawl itcast -o itcast.json
8.保存csv格式
	scrapy crawl itcast -o itcast.csv
	需要在获取的时候 进行解码 .encode("gbk")

9.使用pycharm打开一个爬虫项目

10.编写一个pycharm的启动脚本
	其实就是 scrapy crawl itcast(itcast是爬虫项目)
	代码就是
	cmdline.execute("scrapy crawl itcast".split())

--- 爬取流程

6.爬取网站信息
http://www.itcast.cn/channel/teacher.shtml#ajavaee
先要查看爬取的数据
techer_list = response.xpath('//div[@class="li_txt"]);
for each in techer_list:
	# name
	each.xpath('./h3/text()')
	# title	
	each.xpath('./h4/text()')
	each.xpath('./p/text()')


--- 错误提示
1.如果下载文件没有设置 就需要注释掉
exceptions.NameError: Module 'mySpider.pipelines' doesn't define any object named 'MySpiderPipelines'

2.
    raise URLError(err)
URLError: <urlopen error timed out>
2018-05-19 18:40:43 [boto] ERROR: Unable to read instance data, giving up


