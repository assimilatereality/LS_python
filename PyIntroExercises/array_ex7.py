lst = [1, 'joe', 3.1]

[print(str(x + 1) + '. ' + str(lst[x])) for x in range(len(lst))]

print(lst.index('joe'))

[print(str(x + 1) + '. ' + str(lst[x])) for x, z in enumerate(lst) if z == lst[x]]
