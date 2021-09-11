# HOME WORK

# Problem 1.

list_of_numbers_2 = [3, 5, 15, 2, 9, 11, 10]
ls = []
for x in list_of_numbers_2:
    ls.append(x * 2)

print(ls)

# Problem 2.

list_with_duplicates = ['a', 'b', 'ab', 'a', 'c', 'ab', 'd', 'hh', 'k', 'hh']

for x in list_with_duplicates:
    if list_with_duplicates.count(x) > 1:
        list_with_duplicates.remove(x)

print(list_with_duplicates)

# Problem 3.

ls = [3, 5, 88, -1, 0, -1, 3, -7, -10, 3, 3, -7, 5, -10, 1]
ls.sort(reverse=False)

for x in ls:
    while ls.count(x) > 1:
        ls.remove(x)

print(ls[1])

# Problem 4.

the_list = ['chrome', 'opera', 'mozilla', 'explorer']
string = "AAA"
new_list = []
for x in the_list:
    new_list += [string + x]

print(new_list)

# Problem 5.

n1 = 0
try:
    print(1 / n1)
except ZeroDivisionError:
    print("You cant divide a number by 0.")

# Problem 6.

ll = ["A", "B", "C", "D"]

try:
    print(ll[5])
except IndexError:
    print("list index out of range")

# Problem 7.

# 1 variant.
list_of_list = [['anna', 'bob'], ['john', 'peter'], ['sarah', 'jess', 'ben'], ['ross']]

one_list = []

for x in list_of_list:
    for y in x:
        one_list += [y]

print(one_list)

# 2 variant.

list_of_list = [['anna', 'bob'], ['john', 'peter'], ['sarah', 'jess', 'ben'], ['ross']]

one_list = [y for x in list_of_list for y in x]

print(one_list)
