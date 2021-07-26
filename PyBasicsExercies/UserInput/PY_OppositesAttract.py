def valid_number(number_string):
    return str(int(number_string)) == number_string and int(number_string) != 0


# first_number = 0
# second_number = 0
num = 0


def number(num):
    while num == 0:
        num = input("Enter an integer: ")
        if valid_number(num):
            return num
        else:
            print("Invalid input. Only non-zero integers are allowed.")
            num = 0

while True:
    first_number = int(number(0))
    second_number = int(number(0))
    if first_number * second_number < 0:
        break
    else:
        print("One int must be positive and one int must be negative.")

print(f'{first_number} + {second_number} = {first_number + second_number}')