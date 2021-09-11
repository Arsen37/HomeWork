# HOME WORK

# Problem 1.

f = open(r"C:\Users\arsen\Desktop\DOC.txt", "a")
f.write("black, white , grey")
f.close()

f = open(r"C:\Users\arsen\Desktop\DOC.txt", "r")
print(f.read())

# Problem 2.

with open(r"C:\Users\arsen\Desktop\PATH.txt", "r") as lines:
    x = (lines.readline())
    y = (lines.readline())
    z = (lines.readline())
    u = (lines.readline())
    k = (lines.readline())
print(x, y, z, u, k)

# Problem 3.

f2 = (r"C:\Users\arsen\Desktop\pr3.txt")

with open(f2, 'r') as file:
    words = file.read().split()
    max_len = len(max(words, key=len))
for x in words:
    if len(x) == max_len:
        print(x)

# Problem 4.

nn = ['Ani', 'Armen', 'Aren', 'Arsen', 'Alik']
for z in nn:
    n1 = open(fr"C:\Users\arsen\Desktop\{z}.txt", "w")
    for i in z:
        str(n1.write(z + "\n"))

    n1 = open(fr"C:\Users\arsen\Desktop\{z}.txt", "r")
    print(n1.read())

# Problem 5.  sharunakutyunna 4-i .

new_names = ['Ani', 'Armen', 'Aren', 'Argishti', 'Arsen', 'Alik', 'Anahit', 'Anna']
for x in new_names:
    if x in nn:
        print(x, True)
    else:
        print(x, False)

# Problem 6.

f3 = open(r"C:\Users\arsen\Desktop\pr3.txt")
number = 0
for i in f3:
    for x in i:
        if "A" <= x <= "Z":
            number += 1

print(number)

# Problem 7.

f4 = open(r"C:\Users\arsen\Desktop\GG.txt")
gg = (f4.read().split())
print("Ani appears in the text " + str(gg.count("Ani")) + " times.")
print("Arsen appears in the text " + str(gg.count("Arsen")) + " times.")
print("1 appears in the text " + str(gg.count("1")) + " times.")
print("5 appears in the text " + str(gg.count("5")) + " times.")
