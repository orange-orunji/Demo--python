"""
    re的三个主要方法使用(match，search，findall)
"""
import re
s = "python itcast"
match = re.match("python", s)
print(match)
print(match.span())
print(match.group())
print("-------------------------------")
search = re.search("itcast", s)
print(search)
print(search.group())
print(search.span())
print("-------------------------------")
findall = re.findall("itcast", s)
print(findall)
