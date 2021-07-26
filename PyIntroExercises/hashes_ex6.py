x = 'hi there'
my_hash = {'x': "some value"}
for k,v in my_hash.items():
    print("{}: {}".format(k,v))

# Unlike Ruby, there is no old way and new way
my_hash2 = {'x': "some value"}
for k,v in my_hash.items():
    print("{}: {}".format(k,v))