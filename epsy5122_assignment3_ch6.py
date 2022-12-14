# Aspen Holm
# EPSY 5122
# 9/27/2022

# Assignment 3

# creating a string and asking for certain index positions
fruit = "banana"
letter = fruit[1]
print(letter)
letter = fruit[0]
print(letter)
letter = fruit[1.5]

# using "len" to find length of string
fruit = banana
len(fruit)
length = len(fruit)
last = fruit[length]
last = fruit[length-1]
print(last)

# using slices with strings
s = "Monty Python"
print[0:5]
print(s[6:12])
fruit = "banana"
fruit[1:3]
fruit[3:]
fruit[3:3]

# we can't change an exisitng string
# we can only add onto it
greeting = "Hello, world!"
greeting[0] = "J"
new_greeting = "J" + greeting[1:]
print(new_greeting)

# asking if first string appears in second string
"a" in "banana"
"seed" in "banana"

# using methods with strings
stuff = "Hello world"
type(stuff)
dir(stuff)
word = "banana"
new_word = word.upper()
print(new_word)
index = word.find("a")
print(index)
word.find("na")
word.find("na", 3)
line = "    here we go  "
line.strip()
line = "Have a nice day"
line.startswith("Have")
line.startswith("h")
line.lower()
line.lower().startswith("h")

# finding a specific part of a string and printing it
data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@")
print(atpos)
sppos = data.find(" ",atpos)
print(sppos)
host = data [atpos+1:sppos]
print(host)

# using % with strings to find and replace things
camels = 42
"%d" % camels
"I have spotted %d camels." % camels
"In %d years I have spotted %g %s" % (3, 0.1, "camels")
"%d %d %d" % (1, 2)
"%d" % "dollars"

# mistakes!!!
# when practicing with the "in" function, I accidentally forgot to format the second word (banana) as a string
# now I know that you have to put quotation marks about both the first and second string
# when practicing with the method "startwith", I realized I needed to capitalize the first H to have it agree that the string starts with H
# this reminded me that Python can tell the difference between upper and lowercase
