# EPSY 5122
# IN CLASS WORK
# 10/5/2022

def add2(x):
    if type(x) == int or type(x) == float:
        print("The value of 2 more than", x, "is", x+2)
        return x+2
    else:
        print("ERROR: not the right input")
    print("outside the branches")


people = ["Pythagoras", "Peppa", "Penelope", "Priya", "Pablo"]

# print("Hello", people[0])
# print("Hello", people[1])
# print("Hello", people[2])
# print("Hello", people[3])
# print("Hello", people[4])

for i in range(len(people)):
    print("Hello,", people[i], "!")

for p in people:
    print("Hello,", p, "!")

for i in range(100)
    print("my favorite number is," i)
