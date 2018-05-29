#coding=utf-8
from bs4 import BeautifulSoup
import requests
import time

def captcha(captcha_data):
	with open("captcha.jpg","wb") as f:
			f.write(captcha_data)
	text = raw_input("请输入验证码:")
	return text		

def zhihuLogin():
	# 构建一个session对象,可以保存cookie
	sess = requests.Session()
	# 请求头
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
	# 首先获取登录页面,找到需要post的数据(_sxrf),同时会记录当前页面的cookie值
	html = sess.get("https://www.zhihu.com/signup",headers=headers).text
	# print html	

	bs = BeautifulSoup(html,"lxml")
#旧版已经没用了	
	# 获取之前get的页面里的_xsrf值
	# 
	# _xsrf 作用是防止 csrf攻击 跨站请求伪造，通常叫跨域攻击，是一种利用网络对用户的一种信任机制来做坏事
	# 跨域攻击通常通过 伪装成网站信任的用户请求（利用cookie），盗取用户信息，欺骗web服务器
	# 所以网站通过设置一个隐藏字段来存放这个MD5字符串，这个字符串用来校验用户(cookie和服务器session的一种方式)
	 _xsrf = bs.find("input",attrs={"name":"_xsrf"}).get.value() #这个_xsrf 是旧版的zhihu 现在已经更新没有这个值了


	# 验证码(旧版)
    # 根据UNIX时间戳，匹配出验证码的URL地址
    captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)
    # 发送请求 拿到验证码的数据流
    captcha_data = sess.get(captcha_url,headers = headers).content
   	# 获取验证码里的文字，需要手动输入
    text = captcha(captcha_data)

	data = {
       	"_xsrf" : _xsrf,
        "email" : "123636274@qq.com",
        "password" : "ALARMCHIME",
        "captcha" : text
	}
	Session.post("https://www.zhihu.com/api/v3/oauth/sign_in",data=data,headers = headers)
	print response.text
	




	# 新版的已经不是这样了，zhihu现在已经做了反爬虫，
	# 验证码获取 是每次页面请求都会发送一次验证码请求 如果有返回值，就请求2个请求
	# {"show_captcha":true}
	"""
	{"show_captcha":true}
	请求回来的{"img_base64":"R0lGODdhlgA8AIcAAP7+/gEBAefn5xYWFtbW1vPz8ycnJ8jIyFdXV3d3d4eHh2ZmZkdHRzU1NZaW\nlqenp7e3t7i4uKioqMHBwTs7O0BAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAlgA8AEAI/wABCBxI\nsKDBgwgTKlzIsKHDhxAjOiQwYUGAixgzFojAYIAEAQBCihxJsqTJkyhTqkQpQMGAADBjyoQ5QACA\nmzhz6tzJs6cABwsGBGigQIGBAwCSKl3KVEKApwEGIAgQYECAAAMMNIhwIIDXAAsKABhLFkACAGjT\n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\nbl27dgMCADs=\n"}	
	data:image/jpg;base64,R0lGODdhlgA8AIcAAP7+/gEBAefn5xYWFtbW1vPz8ycnJ8jIyFdXV3d3d4eHh2ZmZkdHRzU1NZaW%0Alqenp7e3t7i4uKioqMHBwTs7O0BAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAlgA8AEAI/wABCBxI%0AsKDBgwgTKlzIsKHDhxAjOiQwYUGAixgzFojAYIAEAQBCihxJsqTJkyhTqkQpQMGAADBjyoQ5QACA%0Amzhz6tzJs6cABwsGBGigQIGBAwCSKl3KVEKApwEGIAgQYECAAAMMNIhwIIDXAAsKABhLFkACAGjT%0A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%0Abl27dgMCADs=
	"""

	"""
	比较
	原始
	找到规律 是把\n 替换成%0A 删除最后一个%0A
	R0lGODdhlgA8AIcAAP7+/gEBAefn5xYWFtbW1vPz8ycnJ8jIyFdXV3d3d4eHh2ZmZkdHRzU1NZaW \nlqenp7e3t7i4uKioqMHBwTs7O0BAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAlgA8AEAI/wABCBxI\nsKDBgwgTKlzIsKHDhxAjOiQwYUGAixgzFojAYIAEAQBCihxJsqTJkyhTqkQpQMGAADBjyoQ5QACA\nmzhz6tzJs6cABwsGBGigQIGBAwCSKl3KVEKApwEGIAgQYECAAAMMNIhwIIDXAAsKABhLFkACAGjT\n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\nbl27dgMCADs=\n
																				 %0Alqenp7e3t7i4uKioqMHBwTs7O0BAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAlgA8AEAI/wABCBxI%0AsKDBgwgTKlzIsKHDhxAjOiQwYUGAixgzFojAYIAEAQBCihxJsqTJkyhTqkQpQMGAADBjyoQ5QACA%0Amzhz6tzJs6cABwsGBGigQIGBAwCSKl3KVEKApwEGIAgQYECAAAMMNIhwIIDXAAsKABhLFkACAGjT%0AqiWgIEAAAxAeLDhgYMAABwYCMBgwgACAvwIKEAhAOACCAgASK17MuAAEAQAiS55MubJlyhMIBNi8%0A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%0Abl27dgMCADs=
	R0lGODdhlgA8AIcAAP7+/gEBAefn5xYWFtbW1vPz8ycnJ8jIyFdXV3d3d4eHh2ZmZkdHRzU1NZaW %0Alqenp7e3t7i4uKioqMHBwTs7O0BAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAlgA8AEAI/wABCBxI%0AsKDBgwgTKlzIsKHDhxAjOiQwYUGAixgzFojAYIAEAQBCihxJsqTJkyhTqkQpQMGAADBjyoQ5QACA%0Amzhz6tzJs6cABwsGBGigQIGBAwCSKl3KVEKApwEGIAgQYECAAAMMNIhwIIDXAAsKABhLFkACAGjT%0A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%0Abl27dgMCADs=
	"""



if __name__ == '__main__':
	zhihuLogin()
