x = 0
while x <= 10:
    if x == 3:
        x += 1
        continue
    elif x % 2 != 0:
        print(x)
    x += 1