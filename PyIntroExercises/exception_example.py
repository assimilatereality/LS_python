names = ['bob', 'joe', 'steve', None, 'frank']

a = [item if item is not None else "" for item in names]
for item in a:
    print(item)
