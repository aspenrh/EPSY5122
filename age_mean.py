ages = [20, 22, 25, 70, 23, 19]

# find the mean
sum_ages = sum(ages)
num_ages = len(ages)
mean_age = sum_ages / num_ages

n_decimals = 2
print("The average age is:", round(mean_age, n_decimals), "years.")

# CHALLENGE:
# print the MAX and MIN with appropriate labels
max_ages = max(ages)
print("The maximum age is:", max_ages, "years.")

min_ages = min(ages)
print("The minimum age is:", min_ages, "years.")


# let's try creating a function...
ages = [20, 22, 25, 70, 23, 19]
def mean(ages):
    sum_ages = sum(ages)
    num_ages = len(ages)
    mean_age = sum_ages / num_ages
    n_decimals = 2
    print("The average age is:", round(mean_age, n_decimals), "years.")

mean([3, 5, 10])
