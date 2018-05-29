#coding=utf-8

import re

pattern = re.compile("\d+")
# pattern = re.compile("\d?")
# pattern = re.compile("\d*")
m = pattern.findall("hello 123456 789")
print m
m = pattern.findall("aaa123bbb456",1,10)
print m


# finditer
m = pattern.finditer("aaa123bbb456")
print m
for i in m:
	# print i
	print i.group()