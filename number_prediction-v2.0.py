#!/usr/bin/env python3
import math

LOWER_BOUND, UPPER_BOUND = 0, 123
QUESTION = 'what is the remainder of the division by 2?'
RETRY_MESSAGE = 'Reminder of division by 2 can be only 0 or 1! Try again'
WRONG_NUMBER_FTM = "Your number is {}! It's wrong because number must be from {} to {}."


def main():
    print_help()
    number = game()
    if number > UPPER_BOUND or number < LOWER_BOUND:
        print(WRONG_NUMBER_FTM.format(number, UPPER_BOUND, LOWER_BOUND))
    else:
        print('Your number is: {}'.format(number))


def game():
    steps_to_finish = int(math.ceil(math.log2(UPPER_BOUND)))
    number = 0
    for i in range(steps_to_finish):
        reminder = get_next_reminder()
        if reminder is None:
            break
        number += int(math.pow(2, i)) if reminder == 1 else 0
    return number


def get_next_reminder():
    print(QUESTION)
    while True:
        print('>>> ', end='')
        line = input()
        if line == '':
            return None
        try:
            reminder = int(line)
        except ValueError:
            reminder = None
        if reminder in (0, 1):
            break
        print(RETRY_MESSAGE)
    return reminder


def print_help():
    print('''
    Hi, I'm a program, divining numbers!
    If I ask, "{}", you have to divide your number by 2 and enter reminder.
    Enter empty line if your number has become 0.
    The number ranges from 0 to 123. Let's start!
    '''.format(QUESTION))


if __name__ == '__main__':
    main()
