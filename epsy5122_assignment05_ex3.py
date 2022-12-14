# Aspen Holm
# EPSY 5122
# 10/11/22

# Assignment 5, exercise 3

inp = input("What is your score?")
score = float(inp)
if score > 1 or score < 0:
    print("out of range!")
elif score >= 0.9:
    print("you get an A!")
elif score >= 0.8:
    print("you get a B")
elif score >= 0.7:
    print("you get a C!")
elif score >= 0.6:
    print("you get a D!")
elif score < 0.6:
    print("you get an F :(")

# mistakes!!!
# honestly, this one took me forever to get it to work because of two mistakes:
# 1. I kept entering scores as whole numbers rather than decimals (ex. 75 instead of 0.75)
# 2. I wrote score = float("inp"), so I kept getting an error message that python couldn't convert "imp" to a float
# but it's because it wasn't reading the variable inp!!! silly me
# I learned that a lot of times code won't run because of tiny mistakes, and sometimes it takes a second to catch those mistakes
