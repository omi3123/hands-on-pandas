# df.isnull() & df.notnull()

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", None],
    "Age": [25, None, 22, 30],
    "City": ["Lahore", "Karachi", None, "Islamabad"]
}
df = pd.DataFrame(data)
print(df.isnull())     
print(df.notnull())     

# Remove Rows with Any Missing Data

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", None],
    "Age": [25, None, 22, 30]
}
df = pd.DataFrame(data)
clean_df = df.dropna()
print(clean_df)

# Fill Missing Values with Default

import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", None],
    "City": ["Lahore", None, "Karachi"]
}
df = pd.DataFrame(data)
df_filled = df.fillna("Unknown")
print(df_filled)
