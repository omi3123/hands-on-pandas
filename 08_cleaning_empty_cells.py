# Remove Rows with Empty Cells

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, None, 22, 30]
}
df = pd.DataFrame(data)
df.dropna(inplace=True)
print(df)

# Fill Empty Cells with Specific Value

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, None, 22, 30]
}
df = pd.DataFrame(data)
df.fillna("Unknown", inplace=True)
print(df)

# Fill with Mean / Median / Mode (numerical columns)

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, None, 22, 30]
}
df = pd.DataFrame(data)
df["Age"].fillna(df["Age"].mean(), inplace=True)   
df["Age"].fillna(df["Age"].median(), inplace=True)  
df["Age"].fillna(df["Age"].mode()[0], inplace=True)  

# Another Example

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, None, 22, 30]
}
df = pd.DataFrame(data)
df["Age"].fillna(df["Age"].mean(), inplace=True)
print(df)
