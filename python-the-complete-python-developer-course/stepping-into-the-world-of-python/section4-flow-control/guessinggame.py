import random

highest = 100
answer = random.randint(1, highest)
guess = 0
print("Please guess number between 1 and {}".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done, yout guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
