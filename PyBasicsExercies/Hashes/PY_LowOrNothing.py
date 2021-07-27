numbers = {
    'high': 100,
    'medium': 50,
    'low': 10
}

newDict = dict()
for (key, value) in numbers.items():
    if value < 25:
        newDict[key] = value

print(newDict)