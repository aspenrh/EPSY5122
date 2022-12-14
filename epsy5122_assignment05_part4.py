# Aspen Holm
# EPSY 5122
# 10/11/22

# Assignment 5 part 4

big_list = list(range(1,101))
for x in big_list:
    if x % 2 == 0:
        print("x is a multiple of 2")
    if x % 3 == 0:
        print("x is a multiple of 3")

# for the group that is only divisible by 2, the for loop prints that x is  a multiple of 2
# for the group that is only divisible by 3, the for loop prints that x is a multiple of 3
# the the group that is divisible by both, the for loop prints that x is a multiple of 2, and in a new line prints x is a multiple of 3
# for the group that is divisible by neither, nothing prints
