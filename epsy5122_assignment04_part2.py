# Aspen Holm
# EPSY 5122
# 10/5/2022

# Assignment 4 Part 2

def months_to_years(age):
    years = age / 12
    return years
months_to_years(12)
months_to_years(97)
months_to_years(400)
months_to_years(503)
months_to_years(503.99)
months_to_years(520235.72)
months_to_years(-5)
months_to_years('ninety')
months_to_years([94, 89])

# the function responds to numbers divisible by 12 with integers
# the function responds to numbers not divisible by 12 with floats, including negatives
# the function does not respond to lists- error message about unsupported operand type
