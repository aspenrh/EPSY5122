# Aspen Holm
# EPSY 5122
# 9/20/2022

# Assignment 2 Exercise 1

ages = ["9", "25", "13", "19", "10", "26", "58", "91", "3"]
inp = input("What age would you like to check is in the list? ")
inp in ages
if inp in ages:
    print("It is true that this number is in the list.")
if inp not in ages:
    print("It is false that this number is in the list.")

# mistakes!!!
# at first, it kept telling me that no matter what number I entered, it wasn't in the list
# then I realized that I needed to put quotation marks around all the items, even though they are also integers
# I learned that in this context, we need to put the items in the list in quotations for Python to understand
