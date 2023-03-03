import pandas as pd
import numpy as np
import seaborn as sb

### Understanding the data
#Load Dataset 
df = pd.read_csv(r'arrhythmia.csv')

#Exploratory Analysis
#print(df.shape)

#print(df.columns)

#print(df.head(10)) #Printing first 10 entries of the dataset

#print(df.info()) # Understanding the different datasets

#print(df.isna().sum()) # Getting null values

print(df.describe()) #show the summary statistics of the numeric variables.