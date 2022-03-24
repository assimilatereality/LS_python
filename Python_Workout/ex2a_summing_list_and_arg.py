def mysum(numbers, num):
    output = 0
    for number in numbers:
        output += number
    output += num
    return output


print(mysum([10, 20, 30, 40], 50))
