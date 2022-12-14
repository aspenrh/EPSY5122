### UMN EPSY 5122 Fall 2022
### Programming for Social Science Researchers
### Jeffrey K. Bye, Ph.D.

# Assignment 10: Due Wednesday, November 16 by 2:30pm

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
import seaborn as sns
import matplotlib as plt


#############
### PROBLEM 1

## 1a) Adapt the code from Problem 1a-1b from Assignment 9 to read in the csv
#       and find the subset for just Schools without missing data (NaNs).
#       Save this as act_sch.
#       Then find the subset of act_sch for just year 2014.
#       Save it as act_sub.
act = pd.read_excel("/Users/aspenholm/Downloads/Minnesota 2018 Public Schools Graduating Class 5 Year Trends.xlsx")
act_sch = act[act["Analysis Level"] == "School"]
act_sch = act_sch[~act_sch.isnull().any(axis=1)]
act_sub = act_sch[act_sch["Grad Year"] == 2014]
print(act_sub)


## 1b) Adapt the code from class to generate a regression-scatter plot for act_sub
#       with Avg Reading scores on the X axis, and Avg Science on the Y axis
#       Use the seaborn package for this (sns.regplot)
#       Save to a png file called act2014.png in a folder called Out_Plots
sns.regplot(data = act_sub, x = "Avg Reading", y = "Avg Sci") \
    .get_figure().savefig("Out_Plots/act2014.png")

## 1c) Run the code below:

# import matplotlib as plt # uncomment this line if you haven't already imported
plt.pytplot.clf() # this will clear the figure
# be sure to use the above line of code after each plot you make below
#   you could use it right after you save a figure to a file
#   or you can use it right *before* you make the subsequent plot


## 1d) Copy-paste the code from 1b and 1c below, then adapt it for 2015
#       Make sure this code saves the file as act2015.png
act_sub2 = act_sch[act_sch["Grad Year"] == 2015]
print(act_sub2)
sns.regplot(data = act_sub2, x = "Avg Reading", y = "Avg Sci") \
    .get_figure().savefig("Out_Plots/act2015.png")
plt.pytplot.clf()


## 1e) Think about the changes you made to the code when completing 1d
#       You probably just changed 2014 to 2015 in a few places, right?
#       Maybe we shouldn't hard-code so much!
#       Rewrite your code from 1d so that it uses the year variable below
#           and creates the files for the year 2016 (remember how to format strings!)
y = 2016
act_sub3 = act_sch[act_sch["Grad Year"] == y]
print(act_sub3)
sns.regplot(data = act_sub3, x = "Avg Reading", y = "Avg Sci") \
    .get_figure().savefig("Out_Plots/act2016.png")
plt.pytplot.clf()



## 1e) Have you guessed yet where we're going with this? (Again!)
#       Create a for-loop below that cycles through the values in the years list
#       Use the code from 1e.
#       It should create and save the regplot for all 5 years
 # (remember this list will stop BEFORE 2019)
# for-loop goes here (might help to use y as the looping variable)
# REMEMBER: you can use the y variable in the filename by using string
#       concatenation or an f-string or similar approach
years = list(range(2014,2019))
for y in years:
    act_sub4 = act_sch[act_sch["Grad Year"] == y]
    print(act_sub4)
    str(y)
    sns.regplot(data = act_sub4, x = "Avg Reading", y = "Avg Sci") \
        .get_figure().savefig(f"act {y} .png")
    plt.pytplot.clf()


#############
### PROBLEM 2

## 2a) Search online for "seaborn change regplot color". Figure out how to change
#       the color of the dots AND the color of the line, both to new (different) colors
#       Copy-paste the code from 1e below and use the color changes.
years = list(range(2014,2019))
for y in years:
    act_sub4 = act_sch[act_sch["Grad Year"] == y]
    print(act_sub4)
    str(y)
    sns.regplot(data = act_sub4, x = "Avg Reading", y = "Avg Sci", scatter_kws = {"color": "orange"}, line_kws = {"color": "pink"}) \
        .get_figure().savefig(f"act {y} .png")
    plt.pytplot.clf()


## 2b) There is a ton of great information on seaborn in its user guide.
#       Here's an example demo: https://seaborn.pydata.org/tutorial/relational.html#relating-variables-with-scatter-plots
#       Go to that link and read a bit. Some of this will likely not make sense yet.
#       That's okay! We are piecing it together.
#       Copy the code in that second block that shows the use of color (hue).
#           section. Paste it below. Now ADAPT it so that it:
#           - uses the act_sch dataframe (with all 5 years present)
#           - shows Avg Math on the x axis
#           - shows Avg Eng on the y axis
#           - uses Grad Year to set the hue
#       Save the file as a png.
sns_fun = sns.relplot(data = act_sch, x = "Avg Math", y = "Avg Eng", hue = "Grad Year")
sns_fun.get_figure().savefig("sns_fun.png")


#############
### PROBLEM 3

## 3a) Just kidding, you're done! This is hopefully a shorter assignment.
#       Congrats on being 2/3 done with the course!

# mistakes!!!
# for some reason I can't get the figure in 2b to save properly...
# I get this error message: AttributeError: 'FacetGrid' object has no attribute 'get_figure'
# this is a weird error that I've never seen before, but I think I did everything right
