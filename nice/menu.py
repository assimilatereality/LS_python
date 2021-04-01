MENU_PROMPT = "Enter a selection: "


def add_movie():
    pass


def show_movies():
    pass


def find_movie():
    pass


user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu()
