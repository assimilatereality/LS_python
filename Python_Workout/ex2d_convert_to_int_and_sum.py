def mysum(*numbers):
    output = 0
    for number in numbers:
        if type(number) == int or type(number) == float:
            output += number
        elif number.isdigit():
            output += int(number)
        else:
            output += 0
    return output


print(mysum('10', 20, '30', '40', 60, 'word'))