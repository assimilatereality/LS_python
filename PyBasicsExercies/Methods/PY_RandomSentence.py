from random import choice

names = ['Dave', 'Sally', 'George', 'Jessica']
activities = ['walking', 'running', 'cycling']

def name(names):
    return choice(names)

def activity(activities):
    return choice(activities)

def sentence(name, activity):
    return name + ' went ' + activity + ' today!'

print(sentence(name(names), activity(activities)))
