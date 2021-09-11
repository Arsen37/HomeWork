# HOME WORK

# Problem 1.

ls = [5, 11, 30, 45, 175, 99, 106, 300, 490, 512, 890, 1000]

for x in ls:
    if x % 5 == 0:
        print(x)
    elif x >= 500:
        break

# Problem 2.

list1 = [1, 2, 3, 4, 5]

for x in reversed(list1):
    print(x)

# Problem 3.

def fac(n):
    while n > 0:
        return n * fac(n-1)
    return 1


n = int(input("Input number and return the factorial: "))
print(fac(n))

# Problem 4.

list = [1, 2, 3, 4, 5, 6]

for x in list:
    if x % 2 == 0:
        print(str(x) + " - index " + str(list.index(x)) + " (even)")
    else:
        print(str(x) + " - index " + str(list.index(x)) + " (odd)")

# Problem 5.

def func(names):
    for x in names:
        num1 = (x.replace("@", " "))
        num2 = (num1.strip())
        for y in num2:
            if y[0] == "A":
                print(num2)


names = [' Anna', "Lily", " Anahit ", "@Bob", "@Ani@", " Luiza@", "@@Armen"]
print(func(names))


# Problem 6.

x = int(input("Input and check if the number is prime: "))

for i in range(2, x):
    if x % i == 0:
        print(str(x) + " is not a prime number")
        break

else:
    print(str(x) + " is a prime number")

# Problem 7.

x = 0
y = "*"
while x < 5:
    print(y)
    y += " *"
    x += 1