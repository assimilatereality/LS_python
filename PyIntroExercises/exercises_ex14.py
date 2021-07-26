from functools import reduce

lst = ['white snow', 'winter wonderland', 'melting ice',
     'slippery sidewalk', 'salted roads', 'white trees']

b = list(reduce(lambda c, d: c + d.split(' '), lst, []))

print(b)