def drop_digits(num, before, after):
    lst = str(num).split('.')
    if before == 0:
        lst[0] = '0'
    else:
        lst[0] = lst[0][-before:]
    lst[1] = lst[1][:after]
    return float('.'.join(lst))


print(drop_digits(123.456, 3, 3))
