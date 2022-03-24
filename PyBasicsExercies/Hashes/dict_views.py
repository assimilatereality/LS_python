D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()   # not a list
print(type(K))
print(K)

print(type(list(K)))   # force a list
print(list(K))

V = D.values()    # also not a list
print(V)
print(list(V))

print(D.items())   # also not a list
print(list(D.items()))

#print(K[0])   # throws an error -- TypeError: 'dict_keys' object is not subscriptable
print(list(K)[0])
