# HOME WORK

# Problem 1.

x = "Bob_is_a_._Programmer"
y = "good"
print(x.replace(".", y))

# Problem 2.

s1 = "qwerty"
s2 = "asdfg"
s3 = "tyu"
s4 = "1234"
s5 = "p"

string1 = s1[:1],s2[:1],s3[:1],s4[:1],s5[:1]
string2 = s1[len(s1)-1],s2[len(s2)-1],s3[len(s3)-1],s4[len(s4)-1],s5[len(s5)-1]
print(string1)
print(string2)

# Problem 3.

def name(name1):
    if len(name1) % 2 != 0:
        return name1.upper()
    return name1


print(name(input("What is your name?: ")))

# Problem 4.

article = """ (CNN)The University of Virginia has disenrolled 238 students for its fall semester on Friday for not 
complying with the university's Covid-19 vaccine mandate, according to a university spokesperson.
UVA requires "all students who live, learn, or work in person at the university" to be fully vaccinated 
for the upcoming 2021-2022 academic year, according to current university Covid-19 policies.
Out of the 238 incoming Fall semester students, only 49 of them were actually enrolled in classes, and the remaining 
189 "may not have been planning to return to the university this fall at all," UVA spokesperson Brian Coy told CNN.
"Disenrolled means you're not eligible to take courses," Coy said. 
He added that students who were enrolled at the university on Wednesday still have a week to update their status 
at which point they can re-enroll.
"""

print("word university appear in text " + str(article.count('university')) + " times.")
print("word vaccine appear in text " + str(article.count('vaccine')) + " times.")
print("word student appear in text " + str(article.count('student') - article.count("students")) + " times.")
print(article.count('university') + article.count('vaccine') + article.count('student') - article.count("students"))
print(article.count("1") + article.count("2") + article.count("3") + article.count("4") + article.count("5"))

# Problem 5.

a = article.find("2021-2022")
b = len("2021-2022")
print(article[a:a + b])


# Problem 6.

def func(z):
    k = int(len(z) / 2)
    return z[:k] + z[k:].upper()


print(func(input("Enter some word: ")))

# Problem 7.

name777 = input("What is your name?: ")
profession = input("What is your future profession?: ")
text = f"I am {name777} and I am a {profession}."
print(text)

# Problem 8.

def digit(d1,d2,d3):
    return f"{d3}{d2}{d1}"


print(digit(input("Enter digit1: "),input("Enter digit2: "),input("Enter digit3: ")))
