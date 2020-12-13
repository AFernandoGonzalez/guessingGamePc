import random


def guess(x):
    random_number = random.randint(1, x)

    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, please try again. Too high')

    print(
        f'Congratulations!!! You have guessed our random number {random_number}.')


guess(20)
