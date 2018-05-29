#coding=utf8

import urllib2

# nginx 配置用户授权登陆参考链接 https://www.cnblogs.com/zhangeamon/p/7843333.html
# 1先安装 htpasswd
# 2配置信息
# 3重启nginx

test = "admin"
password = "lyh165"
webserver = "192.168.229.129"

# 构建一个密码管理对象,可以用来保持和HTTP请求相关的授权账号信息
passwordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 添加授权账号信息,第一个参数realm如果没有制定就写None,后三个分别是站点ip。账号和密码
passwordMgr.add_password(None,webserver,test,password)

# HTTPBasicAuthHandler () HTTP基础验证处理器类
httpauth_handler = urllib2.HTTPBasicAuthHandler(passwordMgr)
# 处理代理基础验证相关的处理器
#proxyauth_handler = urllib2.proxyBasicAuthHandler()

reuqest = urllib2.Request("http://"+webserver)

# 构建自定义opener
opener = urllib2.build_opener(httpauth_handler)
# 添加到全局的urlopen里面
#urllib2.install_opener(opener)

# 有授权验证信息的
response = opener.open(reuqest)
# 没有授权验证信息的
# response = urllib2.urlopen(reuqest) # 直接访问
# 401错误 需要用户验证信息 urllib2.HTTPError: HTTP Error 401: Unauthorized 

print response.read()
