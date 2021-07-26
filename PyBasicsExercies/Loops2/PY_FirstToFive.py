from random import randint

num1 = 0
num2 = 0

while True:
    num1 += randint(0,1)
    num2 += randint(0,1)
    if num1 != 5 and num2 != 5:
        continue
    print('Five was reached!')
    break