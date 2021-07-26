from random import choice

stoplight = choice(['green', 'yellow', 'red'])

if stoplight == 'green':
    print('Go')
elif stoplight == 'yellow':
    print('Slow down')
else:
    print('Stop')
