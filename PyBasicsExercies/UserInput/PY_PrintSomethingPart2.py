
while True:
    ans = input("Do you want me to print 'something'? (y/n) ")
    ans = ans.lower()
    if ans[0].lower() in ['y', 'n']:
        break

if  ans[0].lower() == 'y':
    print('something')