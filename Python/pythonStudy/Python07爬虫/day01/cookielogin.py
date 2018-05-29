# coding=UTF-8
import urllib
import urllib2


url = "http://www.renren.com/228321205/profile"
# GET http://www.renren.com/home HTTP/1.1
headers = {
"Host":"www.renren.com",
"Connection":"keep-alive",
#"Upgrade-Insecure-Requests":"1", #忽略真正不安全的请求 比如https的请求
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Referer":"http://www.renren.com/",
#"Accept-Encoding":"gzip, deflate", 不需要压缩，如果出现压缩会出现乱码 因为压缩传输快，传过来的话 我们看到的是乱码
"Accept-Language":"zh-CN,zh;q=0.9",
"Cookie":"anonymid=jh9et4uu-o9lbeh; depovince=GUZ; _r01_=1; wp_fold=0; _de=5EE7745E9811646AA3F7A2766632561634DF20B0B3AA6FF7; __utma=151146938.1607603767.1526493901.1526493901.1526493901.1; __utmz=151146938.1526493901.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/SysHome.do; ln_uact=liyuhong165@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20151023/1625/main_G5Lf_748d000459f2195a.jpg; __utmb=151146938.9.10.1526493901; jebe_key=7cc86b6e-bb72-42f6-b98f-c1966e01bb3e%7C7ff19d5aaded35b0e09be6910f5fd732%7C1526494154656%7C1%7C1526494144953; _ga=GA1.2.1607603767.1526493901; _gid=GA1.2.1715386069.1526494346; jebecookies=d5ca0904-0066-48aa-a25f-3eaed27f29db|||||; JSESSIONID=abcnD6HmOh9uj8bXzkQnw; ick_login=ddf3f815-a0fa-497d-bf16-6d858632dd2f; p=453a418eb551686731bea063956d890a6; first_login_flag=1; t=bce2186191732e2cc849c6fba118a3956; societyguester=bce2186191732e2cc849c6fba118a3956; id=98159316; xnsid=95d6333b; loginfrom=syshome"

}

request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)

print response.read()
