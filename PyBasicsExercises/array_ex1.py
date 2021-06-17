lst = [1, 3, 5, 7, 9, 11]
number = 5
rst = [x for x in lst if(number in lst) and (x == number)]
print(type(str(number)))
print(rst)

if number in lst:
    print(str(number) + " is a cool number")