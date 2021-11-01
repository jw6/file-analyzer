import pandas as pd
import os

print(os.listdir())


df1 = pd.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","Value"],index=['First', 'Second'])
print(df1)

df2 = pd.DataFrame([{'Name': 'John', 'Suername': 'Johns'}, {'Name': 'Jack'}])
print(df2)

df3 = pandas.read_csv("./supermarkets/supermarkets.csv")
df4 = pandas.read_json("./supermarkets/supermarkets.json")
# set table header row
df5 = pandas.read_csv("./supermarkets/supermarkets.json", header = None)

# set column names
d5.columns = ['ID', 'Address', 'City', 'ZIP', 'Country', 'Name', 'Employees']