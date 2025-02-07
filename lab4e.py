#!/usr/bin/env python3
# Author ID: [161112214]

def is_digits(sobj):
    numbers = '0123456789'
    for char in sobj:
        if char not in numbers:
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')