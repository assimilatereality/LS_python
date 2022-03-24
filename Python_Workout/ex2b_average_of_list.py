def mysum(numbers):
    output = 0
    for number in numbers:
        output += number
    output = output / len(numbers)
    return output


print(mysum([10, 20, 30, 40]))
