# HOME WORK

# Problem 1.

cars = {
    "car1": {"name": "Mercedes",
             "brand": "CLS",
             "model": " C219",
             "year": 2010,
             "color": "White"
             },
    "car2": {"name": "Ford",
             "brand": "Fusion",
             "model": None,
             "year": 2016,
             "color": "White"
             },
    "car3": {"name": "Lexus",
             "brand": "GX",
             "model": 470,
             "year": 2004,
             "color": "Red"
             }
}
print(cars)

# Problem 2.

ls = [['Bob', 45], ['Anna', 4], ['Luiza', 24], ['Martin', 14]]
diction = {}
for x in ls:
    diction.update({x[0]: x[1]})

print(diction)

# Problem 3. kisat........

dt = {'hundred': 100, 'million': 1000000, 'thousand': 1000, 'ten': 10}

for x in list(dt.values()):
    if x != 1000:
        dt.popitem()

print(dt)

# Problem 4.

sampleDict = {
    'employee1': {'name': 'Marine', 'salary': 7500},
    'employee2': {'name': 'Karine', 'salary': 8000},
    'employee3': {'name': 'Narine', 'salary': 6500}
}
sampleDict.update({'employee3': {'name': 'Narine', 'salary': 10000}})
print(sampleDict)


# Problem 5.

def func(dict1):
    average = 0
    for x in dict1.values():
        average += x // len(dict1.values())

    for i in dict1:
        dict1.update({i: average})
    return dict1


print(func({'Ann': 3000,
            'Bob': 4000,
            'Lily': 5000,
            'Molly': 5500,
            'Arsen': 500
            }))

# Homework 7 Problem 4.

the_list = ['chrome', 'opera', 'mozilla', 'explorer']

for x in range(0, len(the_list) * 2, 2):
    the_list.insert(x, "AAA")

print(the_list)

