# ask the user for two numbers
# ask the user for an operation to perform
# perform the operation on the two numbers
# output the result

def prompt(message):
    print(f"=> {message}")


def valid_number(num):
    return int(num) != 0


def operation_to_message(op):
    op = {'1': 'Adding',
          '2': 'Subtracting',
          '3': 'Multiplying',
          '4': 'Dividing'
    }

def add():
    return number1 + number2

def subtract():
    return number1 - number2

def multiply():
    return number1 * number2

def divide():
    return number1 / number2

def invalid():
    pass

prompt("Welcome to the Calculator!")

while True:
    name = input("   Enter your name: ")
    name = name.strip()
    if name == '':
        prompt("Make sure to use a valid name.")
    else:
        break

prompt(f"Hi {name}")

while True:  # main loop
    number1 = ''
    while True:
        number1 = input("--> What's the first number? ")
        if valid_number(number1):
            number1 = float(number1)
            break
        else:
            prompt("Hmm... that doesn't look like a valid number")


    while True:
        number2 = input("--> What's the second number? ")
        if valid_number(number2):
            number2 = float(number2)
            break
        else:
            prompt("Hmm... that doesn't look like a valid number")


    #MENU_PROMPT = "Enter a selection: "
    #input("--> What operation would you like to perform?")
    operator_prompt = {
        "1": ('add',add),
        "2": ('subtract',subtract),
        "3": ('multiply',multiply),
        "4": ('divide',divide)
    }

    for key in sorted(operator_prompt.keys()):
        print(f"{key}: {operator_prompt[key][0]}")

    ans = input("Make a choice: ")
    result = operator_prompt.get(ans,[None,invalid])[1]()
    print(result)
    #prompt(operator_prompt)







    break
