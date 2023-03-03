import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# Understanding the data
# Load Dataset
df = pd.read_csv(r'arrhythmia.csv')

#df = df.dropna(how='any')

# Exploratory Analysis

# print(df.shape)

print(df.columns)

# print(df.head(10)) #Printing first 10 entries of the dataset

# print(df.info()) # Understanding the different datasets

# print(df.isna().sum()) # Getting null values

# print(df.describe())  # show the summary statistics of the numeric variables.

# Data Analysis & Visualization

corr_matrix = df.corr()

# print(corr_matrix["weight"].sort_values(ascending=False)) #Sorting dataset by weight attribute

# print(df.query('height==0')) #Checking if there entries with zero height

sb.set_style('darkgrid')
sb.scatterplot(x=df.weight, y=df.QRS)
plt.title("Heart Rate vs Body Weight")
plt.ylabel("Heart Rate")
plt.xlabel("Body Weight")
plt.show()
