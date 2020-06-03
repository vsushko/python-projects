for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

for i in range(17):
    print("{0:>2} in binary is {0:>02x}".format(i))

x = 0x20
y = 0x0a

print(x)
print(y)
print(x*y)

powers = []

for power in range(15, -1, -1):
    powers.append(2 ** power)

print(powers)

x = int(input("Please enter a number: "))

for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
