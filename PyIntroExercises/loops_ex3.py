def countdown(x):
    if x < 0:
        pass
    else:
        print(x)
        x -= 1
        countdown(x)

countdown(4)
