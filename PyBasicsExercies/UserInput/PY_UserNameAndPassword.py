PWCONSTANT = 'houdini'
USERNAME = 'Bob'



while True:
    name = input("What is your name? ")
    ans = input("What is the password? ")
    if ans == PWCONSTANT and name == USERNAME:
        break
    else:
        print("The credentials are not correct. Try again.")

print("Welcome to my web!")