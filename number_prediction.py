#!/usr/bin/env python3
import random

LOWER_BOUND, UPPER_BOUND = 0, 123


def main():
    # BEGIN STEP 1
    print_help()
    number = generate_random_number()
    # END STEP 1

    win, steps = game(number)
    if win:  # SIGNAL b
        msg = 'You win for {} steps'.format(steps)
    else:  # SIGNAL c
        msg = 'You loose :('
    print(msg)


def game(number):
    dividend = number
    step = 1
    while True:
        # BEGIN STEP 2
        print('step {}> '.format(step), end='')
        line = input()
        try:
            predicted_number = int(line)
        except ValueError:
            dividend = game_step(dividend)  # SIGNAL a
        else:
            break  # SIGNAL b/c
        step += 1
        # END STEP 2
    return predicted_number == number, step


def game_step(dividend):
    print_reminder(dividend % 2)
    return int(dividend / 2)


def print_help():
    print('''
    The number ranges from 0 to 123
    Press enter to get new reminder and divide the number by two
    Enter number to try to guess the number
    ''')


def print_reminder(reminder):
    msg = 'Remainder of the division by 2 is ' + str(reminder)
    print(msg)


def generate_random_number():
    return random.randint(LOWER_BOUND, UPPER_BOUND)


if __name__ == '__main__':
    main()
