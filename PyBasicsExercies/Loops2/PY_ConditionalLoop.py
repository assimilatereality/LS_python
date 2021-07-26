from random import choice

process_the_loop = choice([True, False])

if process_the_loop:
    while True:
        print('The loop was processed.')
        break
else:
    print('The loop was not processed.')
    