from decimal import *


def add_decimals(str1, str2):
    return Decimal(str1) + Decimal(str2)


print(add_decimals('0.1', '0.2'))

print(0.1 + 0.2)