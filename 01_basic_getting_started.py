#1

import pandas as pd
data = {
    'Name': ['Ali', 'Ahmed', 'Zara'],
    'Age': [25, 30, 22]
}
df = pd.DataFrame(data)
print(df)

#2

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
print(df)

#3

import pandas as pd
df = pd.read_csv('filename.csv')  
print(df)

#4

import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Zara", "Ayesha", "Usman", "Sara"],
    "Age": [25, 30, 22, 27, 35, 29],
    "City": ["Lahore", "Karachi", "Islamabad", "Multan", "Faisalabad", "Quetta"]
}
df = pd.DataFrame(data)
print("🔹 df.head():")
print(df.head())  
print("\n🔹 df.tail():")
print(df.tail())
print("\n🔹 df.shape:")
print(df.shape) 
print("\n🔹 df.columns:")
print(df.columns)  
print("\n🔹 df.info():")
print(df.info())