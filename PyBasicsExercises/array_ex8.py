#import numpy as np

lst = [3, 4, 5]

def myfunc(a):
    return(a + 2)

b = map(myfunc, lst)

print(list(b))

lst2 = []
[lst2.append(i + 2) for i in lst]
print(lst2)