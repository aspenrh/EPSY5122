# IN CLASS WORK 10/26/22

import numpy as np
import pandas as pd

# from last class...
# act = np.genfromtxt(fname, delimiter = ",", skip_header = 1)
# act_vars = np.genfromtxt(fname, delimiter = ",", max_rows=1, skip_header=0,
# dtype="str", encoding = "utf-8-sig")

# new stuff!!
fname = "/Users/aspenholm/Downloads/Minnesota 2018 Public Schools Graduating Class 5 Year Trends.xlsx"
act = pd.read_excel(fname)

act.loc[2, "District Name"]
act.iloc[2, 1]
act["District Name"][2]

# CHALLENGE!!!
# 1. grab the Avg Math for row 12
# 2. grab the N for row 15 using a different method
act["Avg Math"][12]
act.loc[15, "N"]

act_sch = act[act["Analysis Level"] == "School"]

# CHALLENGE!!!
# 1. subset act_sch to schools w/ N of 20-80
# 2. find the mean Avg Math score of those schools
between_nums = act_sch[(act_sch.N >= 20) & (act_sch.N <= 80)]
between_nums["Avg Math"].mean()
