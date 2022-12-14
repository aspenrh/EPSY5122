### UMN EPSY 5122 Fall 2022
### Aspen Holm
### 10/28/22

# Assignment 7: Due Tuesday, October 25, 2022 by 2:30pm

# NAME: Aspen Holm

## Instructions
# For problems that require you to write code, write your code in the appropriate section below
# For problems that require you to provide a written response, write your answer as a comment (#)

# You should expect to make mistakes on this assignment. That is part of the learning process.
# Whenever you make a mistake, document the mistake AND what you learned from it in the section AT THE BOTTOM.

# As always, document any help you receive from online or friends.
# You must attempt each problem on your own first though! (Otherwise, you won't learn as well!)


#############
### PROBLEM 1

# Think about a type of small data set you might have in your research, with 2 IV and 1 DV.
#  One of the IVs should be a continuous variable (e.g., how many hours studied) #age
#  and the other IV should be a categorical variable (e.g., type of studying, condition, etc.) #gender identity
#  The DV should be continuous. #response time

## 1a. First, create a LIST of data for 10 participants' values for the CONTINUOUS IV.
#       The data can be completely fictional or real, but they must be FLOATS.
#       Save the list with a variable name that both describes *what* the variable is,
#         and also follows good naming style for readability.
#       In other words, I should be able to understand the gist of the variable from its name.
#       Also add a comment that fully describes what the IV represents.

age_participants = [17.0, 23.0, 26.0, 18.0, 32.0, 40.0, 19.0, 21.0, 23.0, 25.0]
# this IV represents the ages (in years) of the ten participants!

## 1b. Next, create a LIST of data for 10 participants' values for the CATEGORICAL IV.
#       The data can be completely fictional or real, but they must be INTEGERS.
#       Save the list with a variable name that both describes *what* the variable is,
#         and also follows good naming style for readability.
#       The values of the IV should be INTEGERS that represent the different category levels.
#       Also be sure that these IV values are in the SAME ORDER as the IV values from 1a.
#       In other words, I should be able to understand the gist of the variable from its name.
#       Also add a comment that fully describes what the IV represents.
#           E.g., "0" is Control, "1" is Experimental, etc.

gender_participants = [1, 1, 2, 1, 2, 3, 4, 1, 2, 1]
# this is the genders of the ten participants, where 1 is woman, 2 is man, 3 is nonbinary, 4 is other

## 1c. Now create a LIST of participants' 10 DV values (e.g., scores on an exam)
#       The data can be completely fictional or real.
#       Save the list according to the same rules as above.
#       Also be sure that the DV values are in the SAME ORDER as the IV values from 1a.
#       In other words, the 2nd # in the IV list should correspond to the 2nd # in the DV list.
#       Also add a comment that fully describes what the DV represents.

response_time = [0.2, 0.9, 0.4, 1.0, 0.7, 0.8, 0.3, 0.4, 0.5, 0.2]
# this is the response times (in seconds) for a facial recognition task for all ten participants

## 1d. Now put all 3 variables, along with a participant ID/# list (1-10), into a single NUMPY ARRAY.
#       Remember that in class we built numpy arrays with np.array() and it built by ROW.
#       That is, each list we passed np.array() was a row in the 2-D array (matrix).
#       To build your numpy array by COLUMN instead, use np.column_stack() instead.
#       Here's a template:

import numpy as np
part_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_data = np.column_stack([part_id, age_participants, gender_participants, response_time])


## 1e. Print out your numpy array. What do you notice about the data types?
#       What happened to your categorical IV? Subject number?  (Answer below as a comment.)

print(my_data)
# all the integers are shown as decimals without the 0- converted to floats?
# also, all the floats that end in .0 are shown as just a number and the decimal with no zero


#############
### PROBLEM 2

## 2a. Demonstrate two DIFFERENT ways to return the first 4 rows of data from your array.
#          By "different ways", I mean you must type anything differently (it can be similar in concept).

# first way:
print(my_data[0, 0:4])
# second way:
print(my_data[0,:])

## 2b. Index your DV column of the data frame using its column index.

print(my_data[:,3])

## 2c. Index your array to return just the DV for participant #4 only.
#       In other words, you'll be indexing both dimensions and should get ONE number back.

print(my_data[3, 3])

## 2d. Slice your numpy array so that you get all of the data for participant #5.

print([my_data[4,:]])

## 2e. Slice your numpy array so that you get BOTH IVs (but NO DVs) for participants #7-9.

print(my_data[6:9, 1:3])

## 2f. Slice your numpy array so that you get ONLY the categorical IV and the DV
#       and only for participants #3 and #6. (The result should be a 2x2 array.)

print(my_data[(2, 5), (2, 3)])
# this just gives me the categorical IV for #3 and the DV for #6 :(


#############
### PROBLEM 3

## 3a. Use the np.mean() function to find the mean of the DV.
#       Save the DV mean as a variable with a meaningful and readable name, with a comment.

resptime_mean = np.mean(response_time)
resptime_mean_num = 0.54
# the average response time is equal to 0.54
# unsure if you mean to save the actual number as a variable or the function, so I did both!


## 3b. Use the np.mean() function to find the mean of the continuous IV.
#       Save the continuous IV mean as a variable with a meaningful and readable name, with a comment.

partage_mean = np.mean(age_participants)
partage_mean_num = 24.4
# the average participant age is 24.4 years
# again, unsure if you want the number or the function saved as a variable, so I did both :)


#############
### PROBLEM 4

## 4a. Using any spreadsheet program (Excel, Numbers, Google Sheets, etc.),
#       create a spreadsheet with the same 4 column structure as above,
#       but create (fake or real) data for 20 participants.
#       Export the spreadsheet as a .csv (look up how if you don't know).
#       Attach your CSV file to your homework submission.
#       (no need to write anything here for this part)

## 4b. Adapt the code from class to use np.genfromtxt() to load in your CSV.

fname = "epsy5122_assignment7_fakedata.csv"
my_data2 = np.genfromtxt(fname, delimiter = ",", skip_header = 1)
print(my_data2)

## 4c. Use the np.mean() function to find the mean of the DV from your CSV data.
#       Save the DV mean as a variable with a meaningful and readable name, with a comment.

dataresptime_mean = np.mean(my_data2[:,3])
dataresptime_mean_num = 0.445
# the mean response time is 0.445

## 4d. Use the np.mean() function to find the mean of the continuous IV from your CSV data.
#       Save the continuous IV mean as a variable with a meaningful and readable name, with a comment.

dataage_mean = np.mean(my_data2[:,1])
dataage_mean_num = 27.6
# the mean age for participants is 27.6 years



#############
### EXTRA CREDIT

## XCa. Using your Prob 4 data, replace the 2nd participant's DV score with the value np.NaN
#           (Remember that NaN stands for "Not a Number")
#           Note that np.NaN should be typed exactly as is (no quotes)
#           The assignment should be done in ONE line of code.
#           If you're not sure how to replace a value in a numpy array,
#               think about how we did it with lists (or look it up).

## XCb. Now use np.mean() on the DV column of data.
#         What do you get as a result?  Why?

## XCc. Now use np.nanmean() on the DV column of data.
#          What do you get as a result? Why?


#############
### MISTAKE DOCUMENTATION (and lessons learned!)
# this assignment was surprsingly straightforward for the most part, I didn't reallt struggle too much
# the only thing I couldn't figure out is 2f... I can't figure out a way to slice two objects not in a row
# otherwise, I was reminded that you almost always need to use print() when you want python to spit something back at you
# otherwise python just saves it but doesn't give it back to you (ex. with means)
