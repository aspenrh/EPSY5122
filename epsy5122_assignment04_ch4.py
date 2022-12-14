# Aspen Holm
# EPSY 5122
# 10/5/2022

# Assignment 4

# defining function print_lyrics
# defining function repeat_lyrics from print_lyrics
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
print(print_lyrics)
print(type(print_lyrics))
print_lyrics()
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()

# using bruce as our parameter
# defining function print_twice
# using Spam, 17, pi, spam*4, and cos(pi) as our arguments in the print_twice function
# using michael as a variable and using it as an argument
def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice("Spam")
print_twice("17")
import math
print_twice(math.pi)
print_twice("Spam" *4)
print_twice(math.cos(math.pi))
michael = "Eric, the half a bee"
print_twice(michael)

# with fruitful functions, we need to store the result
# because w/ scripts python won't show the result!!!
# we need to use a return statement to tell python to give us the result back
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
math.sqrt(5)
result = print_twice("Bing")
print(result)
print(type(None))
def addtwo(a, b):
    added = a + b
    return added
x + addtwo(3, 5)
print(x)

# mistakes!!!
# I noticed that when defining functions, I kept forgetting the :
# also kept forgetting the () when calling functions
# learned that these two things are necessary when dealing with new functions!!
# otherwise, I thought everything else was pretty straightforward
