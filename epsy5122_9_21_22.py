# IN CLASS WORK for 9/21/22

ages = [20, 22, 25, 70, 23, 19]

# find the mean
sum_ages = sum(ages)
num_ages = len(ages)
mean_age = sum_ages / num_ages

n_decimals = 2
print("The average age is:", round(mean_age, n_decimals), "years.")

# printing max and min
print("The maximum age is:", max(ages), "years.")
print("The minimum age is:", min(ages), "years.")



# a new thing
print("47 / 3 is:", 47/3)
print("47 / 3 is:", round(47/3, 2))

# orrrrr....
result_output = "47 / 3 is: {}"
print( result_output.format( 47/3 ))

# method = a function you access by using a dot, i.e. .format or .split
s = "hello world, python is cool"
print(s.split())

# using f strings
result = 47/3
print("47 / 3 is: {result}")
print(f"47 / 3 is: {result}")

# some formatting things
print("pythin is cool\npython is rad") # this start a new line
print("python is cool\tpython is rad") # this is a tab
print("\a") # this makes Python make the alert sound
print("\U0001F40D") # emojis :) the python emoji!!!
