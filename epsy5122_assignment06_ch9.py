# Aspen Holm
# EPSY 5122
# 10/18/2022

# Assignment 6 Chapter 9

# making a dictionary with numbers in English as the key and the numbers on Spanish
# we can use "in" to find out if something is in a dictionary
eng2sp = dict()
print(eng2sp)
eng2sp["one"] = "uno"
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp["two"])
len(eng2sp)
"one" in eng2sp
"uno" in eng2sp
vals = list(eng2sp.values())
"uno" in vals

# using dictionaries to find how many times a given letter shows up in a word
word = "brontosaurus"
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
counts = {"chuck" : 1, "annie" : 42, "jan" : 100}
print(counts.get("jan", 0))
print(counts.get("time", 0))
word = "brontosaurus"
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)

# we can insert a file and have Python count again how many times a word shows up
# I'm confused on this part bc we haven't learned "try" and "except" yet...
fname = input("Enter the file name: ")
try:
    fhand = open(frame)
except:
    print("File cannot be opened:", fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

# using loops and dictionaries to print out keys (sorted)
# by default, keys are printed in no particular order
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(count.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])

# mistakes!!!
# I didn't really make any mistakes here, it was pretty straighforward :)
# one thing I did learn was that when we ask python to print out all the keys in a dictionary, it does it in no specific order
# this makes sense, because the point of dictionaries isn't really to index, but it's still interesting!
