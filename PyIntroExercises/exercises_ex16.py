contact_data = ['joe@email.com', '123 Main st.', '555-123-4567']

contacts = {'Joe Smith': {}}
fields = ['email', 'address', 'phone']

for (k, v) in contacts.items():
    for x in [x for (x) in fields]:
        contacts[k][x] = contact_data.pop(0)
print(contacts)

# ============
contact_data = [['joe@email.com', '123 Main st.', '555-123-4567'],
                ['sally@email.com', '404 Not Found Dr.', '123-234-3454'],
                ['harold@email.com', '1600 Pennsylvania Ave.', '555-555-5555']]

contacts = {'Joe Smith': {}, 'Sally Johnson': {}, 'Joe Biden': {}}
fields = ['email', 'address', 'phone']

counter = 0
for (k, v) in contacts.items():
    for x in fields:
        contacts[k][x] = contact_data[counter].pop(0)
    counter += 1
print(contacts)
