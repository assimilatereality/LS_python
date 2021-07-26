from random import randint

while True:
    number = randint(0, 100)
    print(number)
    if number in range(0, 10):
        break