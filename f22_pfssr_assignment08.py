### UMN EPSY 5122 Fall 2022
### Programming for Social Science Researchers
### Jeffrey K. Bye, Ph.D.

# Assignment 8: Due Wednesday, November 2, 2022 by 2:30pm

# NAME: Aspen Holm

## Instructions
# For problems that require you to write code, write your code in the appropriate section below
# For problems that require you to provide a written response, write your answer as a comment (#)

# You should expect to make mistakes on this assignment. That is part of the learning process.
# Whenever you make a mistake, document the mistake AND what you learned from it in the section AT THE BOTTOM.

# As always, document any help you receive from online or friends.
# You must attempt each problem on your own first though! (Otherwise, you won't learn as well!)

import numpy as np
import pandas as pd

#############
### PROBLEM 1

## 1a) Repeat the code from Week 8 class to load "Minnesota 2018 Public Schools Graduating Class 5 Year Trends.xlsx"
#       into Python as a Pandas data frame called 'act'
fname = "/Users/aspenholm/Downloads/Minnesota 2018 Public Schools Graduating Class 5 Year Trends.xlsx"
act = pd.read_excel(fname)


## 1b) Repeat the code from Week 8 class to subset the data to only those rows with
#        'School' as the 'Analysis Level'. Be sure you re-number the rows as well.
#      This subset of data should be called 'act_sch'
act_sch = act[act['Analysis Level'] == 'School']
act_sch = act_sch.reset_index(drop = True)


## 1c) Run the line of code below and comment on what you think it does.
#         Be sure to describe what term applies to ".std()"
print(act_sch['Avg Math'].std())
# it is finding the standard deviation of the average math column!


## 1d) Adapt the code below so that instead of printing the value,
#       it saves the value to a variable called 'avg_math'
avg_math = act_sch['Avg Math'].mean()


## 1e) Adapt the code from 1d so that you create a variable called 'avg_eng',
#       which is the mean value from the 'Avg Eng' column in act_sch.
avg_eng = act_sch['Avg Eng'].mean()


#############
### PROBLEM 2

## 2a) Adapt the code from Week 8 class where we generated a Boolean (True/False) Series
#       based on a logical comparison, e.g., act_sch.N > 50
#      For this comparison, the value should be True if that school's Avg Math value
#           is GREATER than the value in 'avg_math', and False otherwise
thing = act_sch[act_sch["Avg Math"] > avg_math]
print(thing)


## 2b) Adapt the code in 2a to create a new column in the act_sch data frame
#       called "AboveAvgMath", which is True if that Avg Math value is greater than avg_math
#      To do this, adapt the code from Week 8 class where we created the new column 'Blah'
#       BUT instead of writing a single value on the right-hand side of the assignment,
#       use your code from 2a that generates a whole Series of bools.
#      This problem may involve some trial and error, as we didn't cover this directly.
#       This is great practice for figuring solving novel problems in your future!
act_sch["AboveAvgMath"] = act_sch["Avg Math"] > avg_math


## 2c) Adapt the code from 2b to create a new column, "AboveAvgEng",
#       which is set to True if that Avg Eng value is greater than avg_eng.
act_sch["AboveAvgEng"] = act_sch["Avg Eng"] > avg_eng


## 2d) Use the sum() function, combined with logicals, to find:
#       The number of schools that are above average in math AND English
#       The number of schools that are above average in math BUT NOT English
#       The number of schools that are above average in English BUT NOT math
#       The number of schools that are *below* average in math AND English
#      NOTES: Remember that at the end of Week 8 class, we covered how to
#                  combine logicals into one statement.
#             Remember that sum() of bools returns the number of Trues.
#             The opposite of  ==  is  !=  ("not" equal)
#      This problem may involve some trial and error, as we didn't cover this directly.
#       This is great practice for figuring solving novel problems in your future!
# above average in math AND english:
print(sum(act_sch["AboveAvgMath"] & act_sch["AboveAvgEng"]))
# 1039 schools

# above average in math BUT NOT english:
act_sch["BelowAvgEng"] = act_sch["Avg Eng"] <= avg_eng
print(sum(act_sch["AboveAvgMath"] & act_sch["BelowAvgEng"]))
# 164 schools

# above average in english BUT NOT math:
act_sch["BelowAvgMath"] = act_sch["Avg Math"] <= avg_eng
print(sum(act_sch["BelowAvgMath"] & act_sch["AboveAvgEng"]))
# 18 schools

# below average in both:
print(sum(act_sch["BelowAvgMath"] & act_sch["BelowAvgEng"]))
# 468 schools


## 2e) What do you notice about the numbers in 2d?  Write 1-2 sentences in a comment here,
#       as well as in the discussion forum for Assignment 8 (you can copy-paste your comment).
#       Your comment should be about interpreting the results in the real world, not just stating them.
#       For extra credit (.5 points, substantially respond to 1+ other student's comments.)

# When looking at the numbers of schools scoring below and above average math and English scores, I notice that a lot of schools score above in both categories, instead
# of scoring above in only math or only English. Similarly, there are a lot of schools that score below in both, rather than scoring below in only math or English. To me,
# this reflects how schools with more resources are likely to score better across different areas, rather than excelling in just one area. This also means that schools
# that are struggling to meet the needs of their students because of a lack of resources are likely to see below-average scores in all areas. At first glance, it might
# just appear that students who are good at math also happen to be good at English, but I think it's probably more of a systemic issue than that.


#############
### PROBLEM 3

# 3a) Remember the csv you made for Assignment 6's weather data, based on the dictionary format?
#     Write code below to read in your csv using pandas.
fname = "/Users/aspenholm/EPSY5122/EPSY5122_assignment06_p2.csv"
weather = pd.read_csv(fname)


# 3b) In a comment of 1-2 sentences, describe whether this makes sense and what this tells you
#       about dictionary/JSON format of data vs. pandas/dataframe format.
#       What are the pros and cons of each?
# This does make sense, and I think the pandas way of doing it is much more efficient and easy to understand.


#############
### PROBLEM 4

## Describe a problem that is relevant to your research that you would like to work on for your final project.
#    Note that this project should take about 15-20 hours of work, but not much more or less than that.
#    The goal here is for you to practice applying what we learn in class to your own work.
#  A data-based project could involve scraping data from the internet (which we will cover), or importing your own data,
#    then processing that data, running statistics, plotting, etc.
#  A more program-based project could involve building a Python program that a user could interact with,
#    by providing text inputs that cause the program to do different things
#    (e.g., a more advanced version of our weather printer)
#  A web-based project could involve collecting data (e.g., frequency of hashtags) from websites,
#    which we will cover in later weeks.
#  This problem is *not* a final draft of your project proposal -- it's just to get an idea of what might work.
#    I will speak with each student individually to help come up with a reasonable final project scope.
#  I expect approximately 4-6 sentences for this first draft of your project idea.
#  Note: if you'd like to work with a partner on this, that's great! But working alone is also great!
#    Please indicate if you already have a partner or are hoping to find one.
#    For those who work w/ a partner, the project should be a bit bigger in scope,
#       and one added benefit of working w/ a partner is increased exposure to using git on a server (e.g., GitLab)
#       (which we will cover later in the semester as well)

# For my final project, I will taking a raw data file from our two-arm restless bandit task in mice. I will then be grabbing the relevant data that I want from this Xcel file
#   and converting them into data that makes more sense and putting them into another data frame with better column names. As of right now, I am planning on taking the reward
#   probability column, the left/right choice columns, reward outcome column, and the x and y coordinates column from the original dataset and creating a new dataframe with
#   these data converted into numbers we can use in data analysis. For example, for the data showing what choice the mouse made, instead of having separate columns for left
#   and right choices, I will create a new column in a dataframe called something like "choice outcome", where 1 = left choice and 2 = right choice. This is kind of the first
#   step of my honors thesis project, so it will be helpful when I am performing data analysis next semester.


#############
### MISTAKE DOCUMENTATION
# I thought this assignment was pretty straightforward, but the only thing I had trouble with was remembering that I need to use the print() function if I want python to
# actually spit something out! but I always have trouble remembering that so that's nothing new
# I also had trouble with 3a because I was trying to use the read_excel() function, before I realized that I need to use read_csv()
# this was a good reminder that I need to pay attention to the types of files things are
