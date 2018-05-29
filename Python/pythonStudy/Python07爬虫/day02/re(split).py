#coding=utf-8
import re
pattern = re.compile(r"[\s\d\\\;]+") # 遇到那些字符会进行切割

# m = pattern.split("a bb\aa;mm;		a")
# m = pattern.split(r"a bb\aa;mm;		a")
m = pattern.split(r"a bb\aa;m1m;	123	a")

print m