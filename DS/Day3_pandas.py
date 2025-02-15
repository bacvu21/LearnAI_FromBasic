
##pandas datastructure --- series,   data frame
import pandas as pd
s = pd.Series([10,20,30], index = ["a", "b", "c"])
data = {"name":["bac","Hoang Anh", "hieu", "quang", "thao", "khoi", "hanh"], "age": ["24", "22", "24", "24", "23","23", "24"]}
# df = pd.DataFrame(data)
# df.to_csv("test.csv", index=False)

# print(df)
df = pd.read_csv("test.csv")
# print(df)
# df = pd.read_excel("read_excel.xlsx")

### viewing data

#print(df.head()) ## this is viewing head
print(df.tail())
#print(df.info)
#print(df.describe())