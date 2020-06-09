fruit = {"orange": "a sweet orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit["lemon"])

bike = {"make": "Honda", "model": "250 dream",
        "colour": "red", "engine_size": 250}

print(bike["engine_size"])
print(bike["colour"])

fruit["pear"] = "an odd shaped apple"
print(fruit["pear"])

fruit["pear"] = "great with tequila"

print(fruit["pear"])

del fruit["lemon"]

print(fruit)

# removes all elements
fruit.clear()

print(fruit)

print(fruit["tomato"])

while True:
    dict_key = input("Please enter a fruit:")
    if dict_key == "quit":
        break
    desctiption = fruit.get(dict_key, "We don't have a " + dict_key)
    # if dict_key in fruit:
    #     desctiption = fruit.get(dict_key)
    #     print(desctiption)
    # else:
    #     print("we don't have a " + dict_key)


for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])

ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + " - " + fruit[f])

for val in fruit.values():
    print(val)

print(fruit.keys())

print(fruit.values())
