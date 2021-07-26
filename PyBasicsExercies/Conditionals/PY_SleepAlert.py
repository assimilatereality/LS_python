from random import choice

status = choice(['awake', 'tired'])

def dowhat():
    if status == 'awake':
        return 'Be productive'
    else:
        return 'Go to sleep'

print(dowhat())