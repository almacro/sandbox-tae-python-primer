"""
Demo:
Frozen Dictionary

As demonstrated by polyrand in https://news.ycombinator.com/item?id=46229467
"""
from types import MappingProxyType

d = {}

d["a"] = 1
d["b"] = 2

print(d)

frozen = MappingProxyType(d)

print(frozen["a"])

# Error:
frozen["b"] = "new"

# NOTE upstream collection remains mutable