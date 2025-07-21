from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['c'] = 3
d['d'] = 4
d['b'] = 2

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['c'] = 3
od['d'] = 4
od['b'] = 2

for key, value in od.items():
    print(key, value)
