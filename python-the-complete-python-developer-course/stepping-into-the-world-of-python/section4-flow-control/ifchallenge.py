name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome club -18-30 holidays, {0}".format(name))
else:
    print("I'm sorry, out holidays are only for cool people")
