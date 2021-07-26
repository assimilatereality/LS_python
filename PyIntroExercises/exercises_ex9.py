h = {'a':1, 'b':2, 'c':3, 'd':4}
print(h['b'])
h['e'] = 5
print(h)
for k in {k:v for (k,v) in h.items() if v < 3.5 }: del h[k]
print(h)
#print(x)