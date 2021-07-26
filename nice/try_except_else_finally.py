def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
        else:
            print("Yes thank you")
            print(result)
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")

ask_for_int()
