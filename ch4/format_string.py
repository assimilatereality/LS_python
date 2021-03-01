format_string = 'Hello {}!'
print(format_string.format('Phoebe'))

name = "Adam"
age = 20
print("{} is {} years old".format(name, age))

format_string = "Hello {1} {0}, you got {2}%"
print(format_string.format('Smith', 'Carol', 75))

format_string = "{artist} sang {song} in {year}"
print(format_string.format(artist='Paloma Faith', song='Guilty', year=2017))

print('|{:25}|'.format('25 characters width'))

print('|{:<25}|'.format('left aligned'))
print('|{:>25}|'.format('right aligned'))
print('|{:^25}|'.format('centered'))
