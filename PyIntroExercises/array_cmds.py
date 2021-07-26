a = [1, 2, 'bob', 4.2, ['d', 'e', 'f']]

a.append('bob')
print(a[4][1])
a.pop(-2)
a.remove(4.2)
print(type(a))
print(set(a))
a.append("")

print(a)
