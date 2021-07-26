def count_sheep():
    num = 5
    numb = 0
    while num >= 0:
        print(numb)
        num -= 1
        numb += 1

count_sheep()

def count_sheep():
    num = 5
    numb = 0
    while num >= 0:
        print(numb)
        num -= 1
        numb += 1
    return 10

print(count_sheep())

def count_sheep():
    num = 5
    numb = 0
    while num >= 0:
        print(numb)
        if numb >= 2:
            return
        num -= 1
        numb += 1

print(count_sheep())