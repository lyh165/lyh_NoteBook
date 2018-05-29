import re

pattern = re.compile("([a-z]+) ([a-z]+)",re.I)

m = pattern.match("Hello world hello Python")


print m.group(0)
print m.group(1)
print m.group(2)