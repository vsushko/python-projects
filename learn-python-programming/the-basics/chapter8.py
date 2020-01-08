import re

print(re.findall('[0-9]+', '16 2-by-4s in rows of 8'))

print(re.findall('[A-Z]+', 'SEND + MORE == MONEY'))

unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}

gen = (ord(c) for c in unique_characters)
print(gen)
print(next(gen))
print(next(gen))

print(tuple(ord(c) for c in unique_characters))


def ord_map(a_string):
    for c in a_string:
        yield ord(c)


print((ord_map(unique_characters)))

# permutations
import itertools

perms = itertools.permutations([1, 2, 3], 2)

print(next(perms))
print(next(perms))
print(next(perms))
print(next(perms))
print(next(perms))

perms = itertools.permutations('ABC', 3)
print(next(perms))
print(next(perms))
print(next(perms))

print(list(itertools.product('ABC', '123')))

print(list(itertools.combinations('ABC', 2)))

names = ['Dora\n', 'Ethan\n', 'Wesley\n', 'John\n', 'Anne\n',
         'Mike\n', 'Chris\n', 'Sarah\n', 'Alex\n', 'Lizzie\n']

names = [name.rstrip() for name in names]

print(sorted(names))
print(sorted(names, key=len))

groups = itertools.groupby(names, len)
print(list(groups))

groups = itertools.groupby(names, len)

for name_length, name_iter in groups:
    print('Names with {0:d} letters:'.format(name_length))
    for name in name_iter:
        print(name)

print(list(range(0, 3)))
print(list(range(10, 13)))
print(list(itertools.chain(range(0, 3), range(10, 13))))
print(list(zip(range(0, 3), range(10, 13))))
print(list(zip(range(0, 3), range(10, 14))))
print(list(itertools.zip_longest(range(0, 3), range(10, 14))))
