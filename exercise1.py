import pandas as pd

#Loading dataset as pandas dataframe
data  = pd.read_csv("exercise_data.csv",index_col=0)

#1.Preview for first five rows
print(data.head())

#2.Display First Three Rows
print(data.iloc[:3])

#3.Selecting specific columns (for example:-units)
print(data.loc[:,"Units"])
print(data.iloc[:,3])

#4.Conditional selection using loc (for example :- selecting units dollars)
print(data.loc[data.Units=="Dollars (millions)"])

#5.Modification of selective data using loc
data.loc[data.Units=="Dollars (millions)","Variable_code"] = "H10"
print(data.loc[:,["Units","Variable_code"]])

