# function mean returns the mean of nums in units
#  INPUTS
#   nums: list of numbers to average
#  OUTPUTS
#   the arithmetic mean of nums
def mean(nums):
    sum_nums = sum(nums)
    n_nums = len(nums)
    mean_nums = sum_nums/n_nums
    return mean_nums

import age_functions as af

def age_convert(age_months, units = "y"):
    if units == "y":
        return age_months / 12
    elif units == "d":
        return age_months * (365 / 12)
    else:
        return "you must specify a unit"

mean_age = af.mean([20, 25])
print(af.age_convert(mean_age))
