ans = 0

while ans < 3 or ans != 'q':
    print("Print a number 3 or higher or 'q' to quit.")
    ans = input("How many lines should be printed? ")

    if ans.lower() == 'q':
        break
    #else:
    ans = int(ans)

    if ans < 3:
        print(f'Your answer must be 3 or greater. Try again.')
    else:
        while ans > 0:
            print(f'Launch School is the best!')
            ans -= 1