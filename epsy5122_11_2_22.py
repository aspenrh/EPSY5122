# IN CLASS WORK 11/1/22

import pandas as pd
import numpy as np

act = pd.read_excel("/Users/aspenholm/Downloads/Minnesota 2018 Public Schools Graduating Class 5 Year Trends.xlsx")
print(act)

mask = act["Analysis Level"] == "School"
act[mask]

act_sch = act.copy().loc[mask]

# CHALLENGE!!!
# 1. take act_sch and subset it to schools with 20-80 students using .loc
# 2. find average Avg Math score for act_sch_20_80
# 3. subset act_sch_20_80 to show only schools scoring above the average from 2
act_sch_20_80 = act_sch.loc[(act_sch.N >= 20) & (act_sch.N <= 80)]
print(act_sch_20_80)
mean = act_sch_20_80["Avg Math"].mean()
math_mask = act_sch_20_80["Avg Math"] > mean
act_sch_20_80[math_mask]
