for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)

for x in range(21):
    if x % 3 != 0 and x % 5 != 0:
        print(x)
