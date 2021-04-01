def user_choice():
    choice = "WRONG"
    while choice.isdigit() == False:
        choice = input("Please enter a number (0-10): ")
    return int(choice)

user_choice()
