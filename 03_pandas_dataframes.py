# Creating a DataFrame from Dictionary

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
print(df)

# Accessing Columns

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
print(df["Name"])        
print(df[["Name", "Age"]])  

# Accessing Rows with .loc and .iloc

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
print(df.loc[0])  
print(df.iloc[1])  

# Adding New Column

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
df["Marks"] = [85, 90, 95]
print(df)

# Deleting a column

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
df.drop("City", axis=1, inplace=True)
print(df)

# Adding new row

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
new_row = {"Name": "Usman", "Age": 28, "Marks": 80}
df.loc[len(df)] = new_row
print(df)
