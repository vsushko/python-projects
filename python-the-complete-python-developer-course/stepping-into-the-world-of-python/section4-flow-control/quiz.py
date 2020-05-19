value = 8
answer = 0

for x in range(1, 13):
    answer = value * x

print("{0} times {1} is {2}".format(x, value, answer))


for value in range(10):
    value = value * 2
    print(value)

for value in range(0, 20, 2):
    print(value)

for value in range(11):
    value = value * 2
    print(value)

asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]

for asteroid in asteroids:
    if asteroid == 9617:
        print("G")
    elif asteroid == 9618:
        print("J")
    elif asteroid == 9619:
        print("T")
        break
    elif asteroid == 9620:
        print("E")
else:
    print("M")


for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)

for x in range(30):
    if x % 3 != 0 or x % 5 != 0:
        print(x)

for x in range(30):
    if x % 3 != 0 and x % 5 != 0:
        print(x)