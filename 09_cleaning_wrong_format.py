# Visualize the example

import pandas as pd
data = {
    "Date": ["2024-01-01", "01-02-2024", "bad_date"],
    "Price": ["100", "200", "two hundred"]
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
print(df)

# Cleaning Currency Strings

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara"],
    "Amount": ["Rs 1000", "Rs  2500 ", "Rs3000"]
}
df = pd.DataFrame(data)
df["Amount"] = df["Amount"].str.replace("Rs", "").str.strip()
df["Amount"] = pd.to_numeric(df["Amount"])
print(df)
# Remove Commas from Numbers

import pandas as pd

data = {
    "Salary": ["10,000", "25,000", "30,500"]
}

df = pd.DataFrame(data)
df["Salary"] = df["Salary"].str.replace(",", "")
df["Salary"] = pd.to_numeric(df["Salary"])
print(df)

# Convert Dates to Proper Format

import pandas as pd
data = {
    "JoinDate": ["2024-01-01", "12-05-2024", "13/05/2024", "Invalid"]
}
df = pd.DataFrame(data)
df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors='coerce')
print(df)

# Remove % Symbol and Convert

import pandas as pd
data = {
    "Growth": ["10%", "15%", "7.5%", "12%"]
}
df = pd.DataFrame(data)
df["Growth"] = df["Growth"].str.replace("%", "")
df["Growth"] = pd.to_numeric(df["Growth"])
print(df)