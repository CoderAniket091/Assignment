# Program to read volume entries from csv and print mean, median and standard deviation

# Importing desired modules
import numpy as n
import pandas as pd

# Read data in csv using pandas module
data_file = pd.read_csv("in.csv")
df = data_file["Volume"]

#Printing mean, median and standard deviation
mean = n.mean(df)
print(f"Mean is {mean}")

median = n.median(df)
print(f"Median is {median}")

standardDeviation = n.std(df)
print(f"Standard deviation is {standardDeviation}")

