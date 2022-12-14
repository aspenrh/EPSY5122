# IN CLASS WORK 10/19/22

# fname = "hello.txt"
# open_file = open(fname)
# hello = open_file.read()
# print(hello)

import numpy as np

fname = "Minn_ACT_Scores.csv"
open_file = open(fname, encoding = "utf-8-sig")
# act0 = open_file.read()
# print(act0)
# print(type(act0))

import csv
act1 = list(csv.reader(open_file))
print(act1)
print(type(act1))

act2 = np.array(act1)
