print(3 * 0.1)

from decimal import *
getcontext().prec = 2
print(Decimal(3) * Decimal(0.1))
