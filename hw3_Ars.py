# HOME WORK

# Problem 1.

def name_salary(name, salary=100000):
    print("Employee named " + name + " earns " + str(salary) + ".")


name_salary("Ars", )
name_salary("Ani ", 450000 )


# Problem 2.

def numbers(number1, number2, number3):
    if number2 < number1 < number3:
        print("Yes! the first number falls between the 2nd and 3rd numbers")
    else:
        print("the first number NOT! falls between the 2nd and 3rd numbers")


numbers(8, 7, 9)


# Problem 3.

def number_123(number1, number2, number3):
    if number1 < number3 and number2 < number3:
        return str(number3) + " is the biggest"
    elif number2 < number1 and number3 < number1:
        return str(number1) + " is the biggest"
    return str(number2) + " is the biggest"


print(number_123(11, 5, 3))

# Problem 4.

import math


def volume_of_cylinder(r, h):
    v = math.pi * r ** 2 * h
    return v


vc = volume_of_cylinder(4, 4)
print("Volume of the cylinder is " + str(vc))


# Problem 5.

def func(number1, number2, operation):
    if number1 == 0 or number2 == 0:
        return "the operation cannot be completed"
    elif operation == "+":
        return "result is " + str(number1 + number2)
    elif operation == "-":
        return "result is " + str(number1 - number2)
    elif operation == "*":
        return "result is " + str(number1 * number2)
    elif operation == "/":
        return "result is " + str(number1 / number2)
    return "the operation cannot be completed"


print(func(2, 2, "/"))
