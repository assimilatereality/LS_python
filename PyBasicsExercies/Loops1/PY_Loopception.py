while True:
    print('This is the outer loop.')

    while True:
        print('This is the inner loop.')
        break

    break

print('This is outside all loops.')
