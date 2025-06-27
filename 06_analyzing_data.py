import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, 30, 22, 28],
    "Marks": [85, 90, 95, 88]
}
df = pd.DataFrame(data)
print(df)

# df.describe() → Numerical stats summary

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, 30, 22, 28],
    "Marks": [85, 90, 95, 88]
}
df = pd.DataFrame(data)
print(df.describe())

# df["Marks"].mean() → Mean of column

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, 30, 22, 28],
    "Marks": [85, 90, 95, 88]
}
df = pd.DataFrame(data)
print(df["Marks"].mean())  

# More Functions

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, 30, 22, 28],
    "Marks": [85, 90, 95, 88]
}
df = pd.DataFrame(data)
df["Marks"].max()      
df["Marks"].min()     
df["Marks"].sum()      
df["Marks"].median()   
df["Marks"].std()  

# Count values in a column

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, 30, 22, 28],
    "Marks": [85, 90, 95, 88]
}
df = pd.DataFrame(data)
print(df["Age"].value_counts())
