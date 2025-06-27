# Visulaize the example

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Usman"],
    "Age": [25, -3, 130, 28],
    "Marks": [88, 105, 92, 80]
}
df = pd.DataFrame(data)
df = df[(df["Age"] >= 0) & (df["Age"] <= 100)]
df.loc[df["Marks"] > 100, "Marks"] = 100
print(df)

# Replace Negative Values with Median

import pandas as pd
data = {
    "Product": ["A", "B", "C", "D"],
    "Quantity": [10, -5, 20, -2]
}
df = pd.DataFrame(data)
median_qty = df[df["Quantity"] >= 0]["Quantity"].median()
df.loc[df["Quantity"] < 0, "Quantity"] = median_qty
print(df)

# Remove Nonsense Names

import pandas as pd
data = {
    "Name": ["Ali", "1234", "Ahmed", "???"],
    "Age": [25, 30, 22, 28]
}

df = pd.DataFrame(data)
df = df[df["Name"].str.isalpha()]
print(df)
