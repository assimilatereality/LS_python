mynums = [1, 2, 3, 4, 5, 6]

# lambda and map:
print(list(map(lambda num: num ** 2, mynums)))

# lambda and filter
print(list(filter(lambda num: num % 2 == 0, mynums)))
