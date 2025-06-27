# Creating a Series from a List

import pandas as pd
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)

# Custom Index in Series

import pandas as pd
data = [10, 20, 30, 40]
index = ["a", "b", "c", "d"]
s = pd.Series(data, index=index)
print(s)

# Accessing Elements

import pandas as pd
data = [10, 20, 30, 40]
index = ["a", "b", "c", "d"]
s = pd.Series(data, index=index)
print(s["b"])
print(s[2])     

# Series from Dictionary

import pandas as pd
data = {"Ali": 90, "Ahmed": 85, "Zara": 95}
s = pd.Series(data)
print(s)

# Mathematical Operations on Series

import pandas as pd
marks = pd.Series([80, 75, 90, 60], index=["Ali", "Ahmed", "Zara", "Usman"])
updated_marks = marks + 5
print("Original Marks:\n", marks)
print("\nUpdated Marks:\n", updated_marks)

# Checking Null Values in Series

import pandas as pd
data = [100, None, 85, None]
s = pd.Series(data, index=["Math", "Physics", "Chemistry", "Biology"])
print("Series:\n", s)
print("\nCheck for nulls:\n", s.isnull())
print("\nCheck for non-nulls:\n", s.notnull())
