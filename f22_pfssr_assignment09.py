### UMN EPSY 5122 Fall 2022
### Programming for Social Science Researchers
### Jeffrey K. Bye, Ph.D.

# Assignment 09: Due Wednesday, November 9 by 2:30pm

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

## 1a) Repeat the relevant code from Week 9's class below, in order to:
#       Load in the *full* CSV/xls file of Minnesota schools' ACT scores,
#       subset the data so the only Analysis Level is 'School',
#       remove all rows with null values (NaNs),
#       and reset the index for row numbers, and save as act_sch
act = pd.read_excel("/Users/aspenholm/Downloads/Minnesota 2018 Public Schools Graduating Class 5 Year Trends.xlsx")
act_sch = act[act["Analysis Level"] == "School"] # analysis level of school
act_sch = act_sch.reset_index(drop = True) # resetting row numbers
act_sch = act_sch[~act_sch.isnull().any(axis=1)] # getting rid of NaNs



## 1b) Find the subset of the data for year 2014 only
#       And save it as a data frame called act_sub
sub = act["Grad Year"] == 2014
act_sub = act[sub]
act_sub = act_sub = act_sub[~act_sub.isnull().any(axis=1)]
act_sub = act_sub.reset_index(drop = True)
act_sub = act_sub.dropna()
print(act_sub)


## 1c) Examine the average Avg ACT Science and Reading scores.
#        First, print out the descriptives stats for each individually
#        (transposing may help)
print(act_sub["Avg Sci"].describe().transpose()) # mean = 22.169
print(act_sub["Avg Reading"].describe().transpose()) # mean = 22.323


## 1d) Adapt the code used above to generate the descriptives,
#	      but this time select the Sci and Reading columns
#         and then use the describe method on them.
#       Then save that object as "sci_read2014”.
#       (Comment on what class of object this is.)
sci_read2014 = act_sub[["Avg Sci", "Avg Reading"]].describe().transpose()


## 1e) Save sci_read2014 as a .csv file to your computer.
sci_read2014.to_csv("math_reading_2014.csv")

#############
### PROBLEM 2

## 2a) Copy-paste the code from 1b, 1d, & 1e below, then adapt it for 2015
sub2 = act["Grad Year"] == 2015
act_sub2 = act[sub2]
act_sub2 = act_sub2 = act_sub2[~act_sub2.isnull().any(axis=1)]
act_sub2 = act_sub2.reset_index(drop = True)
act_sub2 = act_sub2.dropna()
print(act_sub2)
sci_read2015 = act_sub2[["Avg Sci", "Avg Reading"]].describe().transpose()
sci_read2015.to_csv("math_reading_2015.csv")


## 2b) Think about the changes you made to the code when completing 2a
#       You probably just changed 2014 to 2015 in a few places, right?
#       Maybe we shouldn't hard-code so much!
#       Rewrite your code from 2a so that it uses the year variable y below
#           and runs the appropriate code for the year 2016
y = 2016
sub3 = act["Grad Year"] == y
act_sub3 = act[sub3]
act_sub3 = act_sub3 = act_sub3[~act_sub3.isnull().any(axis=1)]
act_sub3 = act_sub3.reset_index(drop = True)
act_sub3 = act_sub3.dropna()
print(act_sub3)
sci_readyear = act_sub3[["Avg Sci", "Avg Reading"]].describe().transpose()
sci_readyear.to_csv("math_reading_year.csv")


## 2c) Have you guessed yet where we're going with this?
#       Create a for-loop below that cycles through the values in the years list
#       Use the code from 2b.
#       It should create and save the descriptives csv for all 5 years
# (remember this list will stop BEFORE 2019)
# for-loop goes here (might help to use y as the looping variable)
years = list(range(2014,2019))
for y in years:
    sub4 = act["Grad Year"] == y
    act_sub4 = act[sub4]
    sci_readyears = act_sub4[["Avg Sci", "Avg Reading"]].describe().transpose()
    sci_readyears.to_csv("math_reading_years.csv")

# mistakes!!!
# there were two main mistakes I made during this assignment:
# 1. I couldn't get the code from 1b to work, but after posting on the discussion page,
# I found out that this is because I was using quotes around the grad year. Yay for
# the discussion page! This makes sense, because since the grad year column
# contains integers, we don't need to use quotes like we do for the analysis level
# column.
# 2. I couldn't figure out how to get descriptive statistics for multiple columns
# at once in 1d. I looked it up on the internet and found a very helpful tutorial
# about how to use the describe() method on multiple columns. Yay for the internet!
# here's a link: https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html



#############
### PROBLEM 3

## 3a) Please go to the Week 11 section in Canvas and make sure you
#       download Anaconda
# done!!

## 3b) Here's our schedule for the remainder of the semester:
# Weeks 10-11 we will learn about notebooks, plots & regression, and some GitHub
# Week 12 we will take a break
# Week 13 we will learn about data from the web, including web scraping
# Week 14 will be active project work, with me meeting w/ each of you to help
# Week 15 we will do final project presentations

# I've posted more information on the final project in the Week 15 module.
#   The key points are:
#   - this is an opportunity for you to stretch your learning toward something
#       that's useful for you -- either for your research or your own interests
#   - think of this as approximately 2-3 homework assignments in length
#   - I care that you learn and have fun -- much more so than any 'final product'
#   - seriously, please have fun with this! it shouldn't add to your stresses

# With this in mind, as well as the list of topics we'll be covering soon,
#   please describe the gist of your idea below (2-3 sentences):

# Essentially, my plan is to take a raw csv file from ABET (where that data
# from our task goes) and create another csv file to import these data to.
# I believe I have everything I need to understand how to do this, i.e. I
# won't really need to use anything from upcoming classes for it.
