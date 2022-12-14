# Aspen Holm
# EPSY 5122
# 9/27/2022

# Assignment 3 exercise 6

# first example: several participants answered "I'm not sure"
# I want to replace all these responses with "N/A"
orig_response = "I'm not sure"
orig_response.replace("I'm not sure", "N/A")
new_response = orig_response.replace("I'm not sure", "N/A")
print(new_response)

# second example: several data entries use a "." to indicate a decimal
# I want to replace these with "," like how the British do it
orig_entry = "578.94"
orig_entry.replace("578.94", "578,94")
new_entry = orig_entry.replace("578.94", "578,94")
print(new_entry)

# third example: one participant entered a smiley face after their answer
# I don't like that, I'm going to tell Python to get rid of that
orig_response = "yes :)"
orig_response.strip(" :)")
new_response = orig_response.strip(" :)")
print(new_response)

# mistakes!!!
# I didn't really encounter many mistakes with this exercise
# one thing that came up was figuring out how to order the code for the methods
# for example, which comes first, the variable name or the method??
# learned that the general format is variable.method
