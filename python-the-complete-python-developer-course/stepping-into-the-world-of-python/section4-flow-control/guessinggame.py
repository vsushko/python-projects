answer = 5

print("Please guess number between 1 and 10")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well doen, yout guessed it")
    else:
        print("Sorry, you have guessed correctly")
else:
    print("You got it first time")
