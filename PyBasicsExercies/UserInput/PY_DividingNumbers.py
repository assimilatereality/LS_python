def valid_number(number_string):
    return str(int(number_string)) == number_string

num1 = -1
num2 = -1

while not valid_number(num1):
    num1 = input("numerator: ")
    if valid_number(num1):
        break

    print(f'The number provided is not a valid number.')

while not valid_number(num2) | int(num2 == 0):
    num2 = input("denominator: ")
    if valid_number(num2) and int(num2) != 0:
        break

    print(f'The number provided is not a valid number.')
if num2 != 0:
    print(f'The 1st, {num1}, divided by the 2nd, {num2} = {int(num1)/int(num2)}')
