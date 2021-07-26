from random import choice

stoplight = choice(['green', 'yellow', 'red'])

driving = {'green': 'Go',
           'yellow': 'Slow down',
           'red': 'Stop'
}

result = driving.get(stoplight, 'orange')

print(result)