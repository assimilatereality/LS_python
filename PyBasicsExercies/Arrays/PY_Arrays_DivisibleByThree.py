numbers = [5, 9, 21, 26, 39]

divisible_by_three = filter(lambda number: (number % 3) == 0, numbers)

print(divisible_by_three)

print(list(divisible_by_three))