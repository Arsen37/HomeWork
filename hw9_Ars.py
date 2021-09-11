# HOME WORK

# Problem 1.

def func(s1):
    s1.clear()
    return s1


print(func({"abgd", }))

# Problem 2.

ss1 = {"black", "white", "red", "orange"}
ss2 = {"red", "green", "white"}

sss1 = list(ss1) + list(ss2)
for x in sss1:
    if sss1.count(x) >= 2:
        ss1.discard(x)
        ss2.discard(x)


print(ss1)
print(ss2)

# Problem 3.

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

for x in test_list:
    if len(x) == 1:
        test_list.remove(x)

print(test_list)

# Problem 4.

tuple1 = (1, 5)
tuple2 = (7, 2)

tp12 = []
for a in tuple1:
    for b in tuple2:
        tp12 += ((a, b), (b, a))

print(tp12)

# Problem 5.

some_tup = (24, 37)
x = float(f"{some_tup[0]}.{some_tup[1]}")
print(x)

# Problem 6.

list1 = [(4, 5, 20, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
ls1 = []
for x in list1:
    ls1.append(tuple(sorted(x)))

print(ls1)