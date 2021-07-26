family = { "uncles": ['bob', 'joe', 'steve'],
           "sisters": ['jane', 'jill', 'beth'],
           "brothers": ['frank', 'rob', 'david'],
           "aunts": ['mary', 'sally', 'susan']
           }


keys = ['brothers', 'sisters']
values = list(map(family.get, keys))
print(values)

new_list = [item for items in values for item in items]
print(new_list)