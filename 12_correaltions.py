# df.corr() → Correlation Matrix

import pandas as pd
data = {
    "Math": [80, 85, 78, 90],
    "Physics": [75, 88, 70, 95],
    "English": [60, 55, 65, 58]
}
df = pd.DataFrame(data)
print(df.corr())

# Positive Correlation

import pandas as pd
data = {
    "Hours_Studied": [1, 2, 3, 4, 5],
    "Marks": [50, 60, 65, 70, 80]
}
df = pd.DataFrame(data)
print(df.corr())

# Negative Correlation

import pandas as pd
data = {
    "Age": [18, 25, 35, 45, 60],
    "Running_Speed": [20, 18, 15, 12, 8]
}
df = pd.DataFrame(data)
print(df.corr())

# No Correlation

import pandas as pd
data = {
    "Temperature": [30, 25, 20, 15, 10],
    "Phone_Calls": [50, 51, 49, 48, 50]
}
df = pd.DataFrame(data)
print(df.corr())