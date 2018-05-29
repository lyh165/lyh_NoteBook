1.爬取的网页
	scrapy shell “url”
2.导入库 LinkExtractor 用来抓取所有相关的链接 。用来去重(去掉重复的链接)
	from scrapy.linkextractors import LinkExtractor
	
	link_list = LinkExtractor(allow=("匹配规则"))
		link_list = LinkExtractor(allow=("start=\d+"))
	link_list.extract_links(response)

3.获取到链接，并且使用规则进行处理 （rules）

4.保存信息到本地 设置log日志



---
开始项目
1.创建项目
2.设置item、pipeline、settings
3.创建模板
	scrapy genspider -t crawl tencent tencent.com





























错误信息(检测url 应该是url填写错误、或者爬取匹配规则错误)
URLError: <urlopen error timed out>
2018-05-20 17:44:43 [boto] ERROR: Unable to read instance data, giving up

2、
2018-05-20 18:08:34 [scrapy] ERROR: Spider error processing <GET https://hr.tencent.com/position.php?start=1690> (referer: https://hr.tencent.com/position.php?start=1660)
Traceback (most recent call last):
  File "/usr/lib/python2.7/dist-packages/scrapy/utils/defer.py", line 102, in iter_errback
    yield next(it)
  File "/usr/lib/python2.7/dist-packages/scrapy/spidermiddlewares/offsite.py", line 28, in process_spider_output
    for x in result:
  File "/usr/lib/python2.7/dist-packages/scrapy/spidermiddlewares/referer.py", line 22, in <genexpr>
    return (_set_referer(r) for r in result or ())
  File "/usr/lib/python2.7/dist-packages/scrapy/spidermiddlewares/urllength.py", line 37, in <genexpr>
    return (r for r in result or () if _filter(r))
  File "/usr/lib/python2.7/dist-packages/scrapy/spidermiddlewares/depth.py", line 54, in <genexpr>
    return (r for r in result or () if _filter(r))
  File "/usr/lib/python2.7/dist-packages/scrapy/spiders/crawl.py", line 69, in _parse_response
    for requests_or_item in iterate_spider_output(cb_res):
  File "/home/share/paichong/day05/TencentSpider/TencentSpider/spiders/tencent.py", line 37, in parseTencent
    item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
IndexError: list index out of range

	
