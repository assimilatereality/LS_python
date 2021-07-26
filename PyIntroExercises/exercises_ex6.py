import numpy as np

def uniq(list1):
    x = np.array(list1)
    print(np.unique(x))

lst = [1,1,2,4,3,4]
uniq(lst)
a_set = set(lst)
print(list(a_set))


