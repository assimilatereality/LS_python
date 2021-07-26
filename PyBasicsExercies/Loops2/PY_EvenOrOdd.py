count = 1

while True:
    if count % 2 == 0:
        print(f'{count} is even.')
    else:
        print(f'{count} is odd.')
    if count == 5:
        break
    count += 1
