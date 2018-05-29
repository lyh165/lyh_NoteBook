#coding=utf-8

import re

pattern = re.compile(r"(\w+) (\w+)")
str = "hello 123, hello 456"
m = pattern.sub("hello world",str)
print m 

m = pattern.sub(r"\2 \1",str)
print m 

pattern = re.compile(r"\d+")
str = "abc123abc456"
m = pattern.sub(r"mmmmm",str)
print m 
