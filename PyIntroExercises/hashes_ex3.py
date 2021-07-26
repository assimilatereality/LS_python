hsh = { 'name': 'bob', 'age': 48, 'wife': 'jane', 'wife_age': 31 }
for k in hsh:
    print(k)
for v in hsh.values():
    print(v)
for k,v in hsh.items():
    print("{}: {}".format(k,v))
print(list(hsh.values()))
print(list(hsh.keys()))
print(hsh)
