# Aspen Holm
# EPSY 5122
# 9/27/2022

# Assignment 3 exercise 5

str = "X-DSPAM-Confidence:0.8475"
str.find("0")
number = str[str.find("0"):]
print(number)
type(number)
float_number = float(number)
print(float_number)
type(float_number)

# mistakes!!!
# at first, I forgot how slicing works and included a second index in the slicing
# then I realized I can just leave the second spot blank so it goes all the way to the end
# I tried to convert the number to a float by just saying float(number)
# then I ealized I need to define a new variable for float(number) that would then be a type float
