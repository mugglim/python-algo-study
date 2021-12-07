"""
# dict is iterable !!

# key : 💥 Only immutable type
- bool, int, float, str, tuple

# value : immutable type or mutable type
"""

dic = {}

# add
dic["name"] = "foo"
dic[(1,2)] = True

# remove
del dic[(1,2)]

# iter
print(dic.keys())
print(dic.values())
print(dic.items())

print(dic)