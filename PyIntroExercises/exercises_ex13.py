lst = ['snow', 'winter', 'ice', 'slippery', 'salted roads', 'white trees']

new_lst = [ x for x in lst if not x.startswith(('s', 'w'))]

print(new_lst)