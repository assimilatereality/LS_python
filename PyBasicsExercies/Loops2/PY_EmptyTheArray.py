import copy

names = ['Sally', 'Joe', 'Lisa', 'Henry']
names_copy = copy.deepcopy(names)

for name in names_copy:
    print(name)
    names.pop(0)
    print(names)
    print(names_copy)