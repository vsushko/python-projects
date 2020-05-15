low = 1
high = 1000

print("Please think of a number between {} and {}")
input("Press ENTER to start")

guess = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Ener h or l, or c if my guess was correct"
                     .format(guess)).casefold()
    if high_low == "h":
      # Guess highere. The low end of thee range becomes 1 greater than the guess.
    elif high_low == "l":
        pass
    elif high_low == "c":
        print("I got it in {} guesses!".format(guess))
    else:
        print("Please enter h, l or c")
