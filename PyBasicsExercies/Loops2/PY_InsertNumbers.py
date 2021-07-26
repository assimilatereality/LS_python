numbers = []

while True:
    num = int(input("Enter any integer: "))
    numbers.append(num)
    if len(numbers) == 5:
        break

print(numbers)
