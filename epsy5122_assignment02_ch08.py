# Aspen Holm
# EPSY 5122 Assignment 2
# 9/20/2022

# Chapter 4 of PY4E

# creating two new lists using integers or strings
[10, 20, 30, 40]
["crunchy frog", "ram bladder", "lark vomit"]

# creating a list using a mix of strings, integers, floats, and another list
["spam", 2.0, 5, [10, 20]]

# empty list
[]

# creating several lists with variables, and then printing them all
cheeses = ["cheddar", "edam", "gouda"]
numbers = [17, 23]
empty = []
print(cheeses, numbers, empty)

# print the first item in the cheese list
print(cheeses[0])

# creating a list called numbers and reassigning the second number to be 5
numbers = [17, 23]
numbers[1] = 5
print(numbers)

# creating a list of cheeses and then asking whether or not certain items are in the list
cheeses = ["cheddar", "edam", "gouda"]
"edam" in cheeses
"brie" in cheeses

# we can use the + to combine lists together, in this case creating a list c which combines a and b
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# we can use the * to repeats a list however many times we want
[0] * 4
[1, 2, 3] * 3

# we can use the : to slice a list from a certain item to another
# if we do not specify a first index, the slice starts at the beginning of the list
# if we do not specify the second index, the slice goes all the way to the end of the list
t = ["a", "b", "c", "d", "e", "f"]
t[1:3]
t[:4]
t[3:]

# if you omit both indexes, the slice is the entire list
t[:]

# we can reassign multiple items in a list by specifying a slice and the items we want to use instead
t = ["a", "b", "c", "d", "e", "f"]
t[1:3] = ["x", "y"]
print(t)

# using append on a list adds a new item to the end of the list
t = ["a", "b", "c"]
t.append("d")
print(t)

# using extend on a list can add one list to the end of another
t1 = ["a", "b", "c"]
t2 = ["d", "e"]
t1.extend(t2)
print(t1)

# we can use sort on a list to sort the items from low to high
t = ["d", "c", "e", "b", "a"]
t.sort()
print(t)

# we can use pop to remove an item from a list, but still be able to see that item
t = ["a", "b", "c"]
x = t.pop(1)
print(t)
print(x)

# we can use del to removd an item from a list when we don't need to see the deleted value
t = ["a", "b", "c"]
del t[1]
print(t)

# we can use remove to remove a certain item by name from the list
t = ["a", "b", "c"]
t.remove("b")
print(t)

# if we wanr to remove multiple items from a list, we can use del and slices together
t = ["a", "b", "c", "d", "e", "f"]
del t[1:5]
print(t)

# here, we are converting a string to a list of characters that make up the string
s = "spam"
t = list(s)
print(t)

# we can use split to break a string of words into individual words
# we can also use slices to look at a specific word in the list
s = "pining for the fjords"
t = s.split()
print(t)
print(t[2])

# we can use delimiter to tell Python where to split an object into words
s = "spam-spam-spam"
delimiter = "-"
s.split(delimiter)

# we can also use delimiter to tell Python where to join a list of strings into one
t = ["pining", "for", "the", "fjords"]
delimiter = " "
delimiter.join(t)

# here, we are asking Python to tell use whether a and b name the same object
a = "banana"
b = "banana"
a is b

# here, we are asking whether or not lists a and b are referring to the same object
a = [1, 2, 3]
b = [1, 2, 3]
a is b

# here, we are defining list a, and then saying that b and a both refer to the same object
a = [1, 2, 3]
b = a
b is a

# here, since a and b both refer to the same object, we can use them interchangeably
b[0] = 17
print(a)

# this won't work, since we will get None in return
word = word.strip()
t = t.sort()

# these are all correct ways of adding an element to a list...
t.append(x)
t = t + [x]

# and these are all incorrect ways
t.append([x])
t = t.append(x)
t + [x]
t = t + x

# we can make copies so that we can retain the original list as well as the modified version
orig = t[:]
t.sort()

### mistakes!!!
# I had a bit of a struggle once again getting my file to load into Python
# I figured it out by watching the class recording and seeing again how to copy and paste the file path
