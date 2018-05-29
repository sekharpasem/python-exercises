# Exit example
import sys

while True:
    print('Type exit to exit the program')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
