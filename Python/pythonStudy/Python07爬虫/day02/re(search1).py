import re

pattern = re.compile(r"\d+")

# m = pattern.search(r"aaa123bbb456") # 123
m = pattern.search(r"aaa123bbb456",2,5) # 12
print m.group()
print m.span()

m = pattern.search(r"hello 123456 789")
print m.group()
print m.span()
