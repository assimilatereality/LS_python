ans = 0

while ans < 3:
    ans = int(input("How many lines should be printed? "))

    if ans <3:
        print(f'Your answer must be 3 or greater. Try again.')

while ans > 0:
    print(f'Launch School is the best!')
    ans -= 1


