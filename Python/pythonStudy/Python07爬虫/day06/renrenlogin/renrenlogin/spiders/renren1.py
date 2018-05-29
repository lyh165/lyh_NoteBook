# -*- coding: utf-8 -*-
import scrapy

# 只要是需要提供post数据的，就可以用这种方法，
# 下面示例：post数据是账户密码
class Renren1Spider(scrapy.Spider):
    name = "renren1"
    allowed_domains = ["renren.com"]

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
		# 这里可以发送请求获取登录时候的参数
		# 比如 
		# _xsrf = response.xpath("//_xsrf").extract()[0]
        yield scrapy.FormRequest(
                url = url,
                formdata = {"email" : "liyuhong165@163.com", "password" : "lyh5992858."},
                #formdata = {"email" : "liyuhong165@163.com", "password" : "lyh5992858.","_xsrf" = _xsrf},
                callback = self.parse_page)

    def parse_page(self, response):
        with open("mao2.html", "w") as filename:
            filename.write(response.body)
