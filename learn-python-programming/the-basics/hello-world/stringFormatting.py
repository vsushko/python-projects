__author__ = 'dev'

age = 11
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

print("""February: {0}
March: {1}
April: {1}
""".format(1, 2))

print("My age is %d years" % age)
print("My age is %d, %s, %d %s years" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print("Pi is approximately %12.50f" % (22 / 7))

for i in range(1, 12):
    print("No. {0:2} squared is %4d and cubed is {2:4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12.50}".format(22 / 7))
