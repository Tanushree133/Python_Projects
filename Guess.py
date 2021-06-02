import random

def guess(x):
    random_no = random.randint(1, x)
    guess = 0
    while guess != random_no:
        guess = int(input(f"Guess a no between 1 and {x} : "))
        if guess < random_no:
            print('Too low!Guess again.')
        elif guess > random_no:
            print('Too high!.Guess again.')
    print(f'Congrats.Right answer : {random_no}')


guess(10)
