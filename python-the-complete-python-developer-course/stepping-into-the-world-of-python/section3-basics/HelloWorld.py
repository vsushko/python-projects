greeting = "Hello"
name = input("Please enter your name ")
print(greeting + ' ' + name)

splitString = "This string has been\n split over \n several\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\5\t"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh... he\'s resting"')

anotherSplitString = """This string has been \
split over \
several lines \
"""

print(anotherSplitString)

name = "Bob"
age = 24
greeting = "Hello!"
print(type(age))
print(type(greeting))

print(name + " is " + str(age) + " years old")
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7: 12.50f}")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")