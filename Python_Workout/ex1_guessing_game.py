from random import randint


def guessing_game():
    num = randint(0, 100)
    guess = int(input("What number was produced? "))

    while True:
        if guess > num:
            print(f'Too high')
        elif guess < num:
            print(f'Too low')
        else:
            print(f'Just right')
            break
        guess = int(input("Try again: "))


guessing_game()

