# Aspen Holm
# EPSY 5122
# 10/11/22

# Assignment 5 part 3

def grade(score):
    if score >= 90:
        print("Great job!")
        return("A")
    else:
        print("you got this!")
        return("B")
grade(94)
grade(90)
grade(89)
grade(80)
grade(72)
grade(102)
grade(520235.72)
grade(-5)
grade('ninety')
grade([94, 89])

# the function liked all the inputs up until "ninety" and [94, 89]
# this is because these two are not ints or floats, so python doesn't know what to do with them
