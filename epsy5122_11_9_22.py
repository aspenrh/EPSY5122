# IN CLASS WORK 11/9/22

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

act = pd.read_excel("/Users/aspenholm/Downloads/Minnesota 2018 Public Schools Graduating Class 5 Year Trends.xlsx")

act_sch = act.copy().loc[act["Analysis Level"] == "School"]
act_sch2 = act_sch.dropna()

def zscore(nums):
    sd = nums.std()
    m = nums.mean()
    z = (nums - m) / sd
    return z
act_sch2["Avg Math Z"] = zscore(act_sch2["Avg Math"])
print(act_sch2[["Avg Math", "Avg Math Z"]])

act_sch2.loc["Avg Math Z by Year"] = act_sch2.groupby("Grad Year")["Avg Math"].transform(zscore)

act_sch2.to_csv("school_act_data.csv")

# plots!!!
plot = act_sch2[["Avg Math", "Grad Year"]].boxplot(by = "Grad Year")
plot.get_figure().savefig("boxplot.png")

plt.pyplot.clf()

plot = act_sch2[["Avg Math Z", "Grad Year"]].boxplot(by = "Grad Year")
plot.get_figure().savefig("boxplot_z.png")

# plt.pyplot.clf()

# plot = act_sch2[["Avg Math Z by Year", "Grad Year"]].boxplot(by = "Grad Year")
# plot.get_figure().savefig("boxplot_z_yr.png")

plt.pyplot.clf()

act2018 = act_sch2.copy()[act_sch2["Grad Year"] == 2018]
act2018_plot = act2018[["Avg Math"]].plot.hist()
act2018_plot.get_figure().savefig("math_plot_hist.png")

plt.pyplot.clf()

act2018_plot = act2018[["Avg Math", "Avg Eng"]].plot.hist(alpha = 0.5)
act2018_plot.get_figure().savefig("plot_hist.png")

plt.pyplot.clf()

math_plot = sns.histplot(act_sch2["Avg Math"])
math_plot.set_title("Average ACT Math Scores")
math_plot.get_figure().savefig("math_plot_hist2.png")

plt.pyplot.clf()

sns.histplot(data = act_sch2, x = "Avg Math", kde = True) \
    .set_title("Average ACT Math Scores") \
    .get_figure().savefig("math_plot_hist2b")

plt.pyplot.clf()

sns.regplot(data = act_sch2, x = "Avg Math", y = "Avg Eng") \
    .get_figure().savefig("math_eng_regplot.png")
