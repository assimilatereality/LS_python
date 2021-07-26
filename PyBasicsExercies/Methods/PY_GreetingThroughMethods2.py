def hello():
    return "Hello"

def world():
    return "World"

def greet():
    return hello() + ' ' + world()

print(greet())