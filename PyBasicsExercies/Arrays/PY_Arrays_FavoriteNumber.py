import itertools

favorites = [['Dave', 7, 'oops'], ['Miranda', 3], ['Jason', 11]]
flattened_favorites = list(itertools.chain(*favorites))

print(flattened_favorites)
