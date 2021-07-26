lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_lst = []
for x in lst:
    if x % 2 == 1:
        new_lst.append(x)
print(new_lst)
