a = 7
array = [1, 2, 3]

def my_value(ary, a):
  for b in ary:
    #p b
    # p a
    #a += b
    a = a + b
    print(a)
    #return a


my_value(array, a)
print(a)