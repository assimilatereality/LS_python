critter = { 'name': 'Oliver' }
animal = { 'type': 'cat' }

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

m1 = Merge(critter, animal)
print(m1)
print(critter)
print(animal)

m2 = critter.update(animal)
print(m2)
print(critter)
print(animal)
