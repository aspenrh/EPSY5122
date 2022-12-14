# Aspen Holm
# EPSY 5122
# 10/11/22

# Assignment 5 Chapter 3

# using Boolean expressions
# the class of True and False
5 == 5
5 == 6
type(True)
type(False)
x != y
x > y
X < y
X >= y
x <= y
x is y
x is not y

# using logical operators
# any non-zero number is interpreted as True, so this expression is true
17 and True

# using if statements
# pass statement does nothing
if x > 0:
    print("x is positive")
if x < 0:
    pass
x = 3
if x < 10:
    print("small")

# using if and else
if x%2 == 0:
    print("x is even")
else:
    print("x is odd")

# using if then and elif
# i.e. chained conditional
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y are equal")
if choice == "a":
    print("bad guess")
elif choice == "b":
    print("good guess")
elif choice == "c":
    print("close but not correct")

# nested conditionals
# this one uses three branches
# nested conditionals are clunky but can sometimes be replaced w/ logical operators
if x == y:
    print("x and y are equal")
else:
    if x > y:
        print("x is less than y")
    else:
        print("x is greater than y")
if x < 0:
    if x < 10:
        print("x is a positive single digit number")
if 0 < x and x < 10:
    print("x is a positive single-digit number")

# mistakes!!!
# no mistakes this time! yay!
# I learned that you have to use colons after "if" statements, and also that you can nest conditionals but should probably avoid it if possible
