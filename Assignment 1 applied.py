# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 01:10:37 2022

@author: shahgee
"""
#importing some libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

height = pd.read_csv("Height of Male and Female by Country 2022.csv")
print(height)
#Taking sample of data
Sample1 = height.iloc[0:6]
print(Sample1)
#part 1

plt.figure()
plt.plot(Sample1["Country Name"], Sample1["Male Height in Ft"], label = "Male Height in Ft")
plt.plot(Sample1["Country Name"], Sample1["Female Height in Ft"],
         label = "Female Height in Ft")
plt.xlabel("Country Name")
plt.ylabel("Height in Ft")
plt.title("male and female height")
plt.legend()
plt.savefig("lineplot.png")
plt.show()

#part 2(a)

plt.figure()
plt.hist(height["Male Height in Ft"], alpha = 0.4, density = True,bins = 20, label="Male Height in Ft")
plt.hist(height["Female Height in Ft"],density = True ,bins = 20,label="Female Height in Ft")
plt.xlabel("height in ft")
plt.ylabel("No of occurance")
plt.title("male and female height")

plt.legend(loc = "upper right")
plt.savefig("histogram.png")
plt.show()

#part 2(b)

plt.figure()
plt.boxplot([height["Male Height in Ft"], height["Female Height in Ft"]])
plt.xticks([1, 2], labels = ["male height","female height"])
plt.ylabel("height in ft")
plt.title("male and female height")
plt.savefig("boxplot.png")
plt.show()