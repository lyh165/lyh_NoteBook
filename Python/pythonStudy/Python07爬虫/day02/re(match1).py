#coding=utf-8

import re

pattern = re.compile("\d+")

m = pattern.match("aaa123456",3,6)
#print m
print m.group()