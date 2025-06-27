# Read a CSV File

import pandas as pd
df = pd.read_csv('data.csv')  
print(df)

# Check Top/Bottom Rows

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())    
print(df.tail())      

# Read Only First N Rows

import pandas as pd
df = pd.read_csv('data.csv', nrows=3)
print(df)

# Set Index Column While Reading

import pandas as pd
df = pd.read_csv('data.csv', index_col='ID')
print(df)

# Handle Missing Values

import pandas as pd
df = pd.read_csv('data.csv', na_values=["N/A", "Not Available", "--"])
print(df)