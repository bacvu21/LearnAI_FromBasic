
#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd 

#load Dataset 

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#read first 5 rows 
# print("First 5 rows:\n   ", df.head())
#print("last 5 rows:\n", df.tail())

selected_column = df[["species","sepal_length"]]  # select a column inside the bracket

filter_colum = df[(df["petal_width"] > 0.5) & (df["species"] == "setosa")]


print(filter_colum)




# print(df)

