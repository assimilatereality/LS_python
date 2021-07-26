from random import randint

numbers = []

while len(numbers) < 5:
    numbers.append(randint(0, 100))

print(numbers)