import pandas as pd

df1 = pd.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","Value"],index=['First', 'Second'])
print(df1)

df2 = pd.DataFrame([{'Name': 'John', 'Suername': 'Johns'}, {'Name': 'Jack'}])
print(df2)