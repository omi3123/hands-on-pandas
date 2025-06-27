# Visualize the example

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Ali", "Zara", "Ahmed"],
    "Age": [25, 30, 25, 22, 30]
}
df = pd.DataFrame(data)
df.drop_duplicates(inplace=True)
print(df)

# Detect & Count Duplicate Rows

import pandas as pd
data = {
    "Name": ["Ali", "Ali", "Zara", "Zara", "Usman"],
    "Age": [25, 25, 22, 22, 30]
}
df = pd.DataFrame(data)
print(df.duplicated())
print("Duplicates found:", df.duplicated().sum())

# Keep Only Last Occurrence

import pandas as pd
df = pd.DataFrame({
    "Email": ["a@example.com", "b@example.com", "a@example.com"]
})
df = df.drop_duplicates(keep="last")
print(df)

# Drop Duplicates Based on One Column Only

import pandas as pd
df = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Ali", "Ali", "Zara", "Zara"],
    "Marks": [80, 90, 85, 85]
})
df = df.drop_duplicates(subset=["Name"])
print(df)
