# import pandas as pd

# data = {
#     'Name': ['Ali', 'Ahmed', 'Zara'],
#     'Age': [25, 30, 22]
# }

# df = pd.DataFrame(data)

# print(df)


# import pandas as pd

# data = {
#     "Name": ["Ali", "Ahmed", "Zara"],
#     "Age": [25, 30, 22],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# }

# df = pd.DataFrame(data)

# print(df)



# import pandas as pd
# df = pd.read_csv('filename.csv')  
# print(df)


# import pandas as pd

# Sample data
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Ayesha", "Usman", "Sara"],
#     "Age": [25, 30, 22, 27, 35, 29],
#     "City": ["Lahore", "Karachi", "Islamabad", "Multan", "Faisalabad", "Quetta"]
# }


# df = pd.DataFrame(data)

# print("🔹 df.head():")
# print(df.head())  

# print("\n🔹 df.tail():")
# print(df.tail())
# print("\n🔹 df.shape:")
# print(df.shape) 
# print("\n🔹 df.columns:")
# print(df.columns)  
# print("\n🔹 df.info():")
# print(df.info())






# # Creating a Series from a List

# import pandas as pd
# data = [10, 20, 30, 40]
# s = pd.Series(data)
# print(s)

# # Custom Index in Series

# import pandas as pd
# data = [10, 20, 30, 40]
# index = ["a", "b", "c", "d"]
# s = pd.Series(data, index=index)
# print(s)

# # Accessing Elements

# import pandas as pd
# data = [10, 20, 30, 40]
# index = ["a", "b", "c", "d"]
# s = pd.Series(data, index=index)
# print(s["b"])
# print(s[2])     

# # Series from Dictionary

# import pandas as pd
# data = {"Ali": 90, "Ahmed": 85, "Zara": 95}
# s = pd.Series(data)
# print(s)

# 

# import pandas as pd
# data = [100, None, 85, None]
# s = pd.Series(data, index=["Math", "Physics", "Chemistry", "Biology"])
# print("Series:\n", s)
# print("\nCheck for nulls:\n", s.isnull())
# print("\nCheck for non-nulls:\n", s.notnull())



# Creating a DataFrame from Dictionary

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara"],
#     "Age": [25, 30, 22],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# }
# df = pd.DataFrame(data)
# print(df)

# # Accessing Columns

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara"],
#     "Age": [25, 30, 22],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# }
# df = pd.DataFrame(data)
# print(df["Name"])        
# print(df[["Name", "Age"]])  

# # Accessing Rows with .loc and .iloc

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara"],
#     "Age": [25, 30, 22],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# }
# df = pd.DataFrame(data)
# print(df.loc[0])  
# print(df.iloc[1])  

# # Adding New Column

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara"],
#     "Age": [25, 30, 22],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# }
# df = pd.DataFrame(data)
# df["Marks"] = [85, 90, 95]
# print(df)

# # Deleting a column

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara"],
#     "Age": [25, 30, 22],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# }
# df = pd.DataFrame(data)
# df.drop("City", axis=1, inplace=True)
# print(df)

# # Adding new row

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara"],
#     "Age": [25, 30, 22],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# }
# df = pd.DataFrame(data)
# new_row = {"Name": "Usman", "Age": 28, "Marks": 80}
# df.loc[len(df)] = new_row
# print(df)




# # Read a CSV File

# import pandas as pd
# df = pd.read_csv('data.csv')  
# print(df)

# # Check Top/Bottom Rows

# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.head())    
# print(df.tail())      

# # Read Only First N Rows

# import pandas as pd
# df = pd.read_csv('data.csv', nrows=3)
# print(df)

# # Set Index Column While Reading

# import pandas as pd
# df = pd.read_csv('data.csv', index_col='ID')
# print(df)

# # Handle Missing Values

# import pandas as pd
# df = pd.read_csv('data.csv', na_values=["N/A", "Not Available", "--"])
# print(df)




# # Read JSON File in Pandas

# import pandas as pd
# df = pd.read_json('data.json')
# print(df)

# # JSON Not Structured as List?

# import pandas as pd
# import json
# with open('data.json') as f:
#     data = json.load(f)
# df = pd.json_normalize(data)
# print(df)

# # Deeply Nested JSON

# # Suppose json file contains:
# [
#   {
#     "ID": 1,
#     "Student": {
#       "Name": "Ali",
#       "Details": {"Age": 20, "City": "Lahore"}
#     }
#   },
#   {
#     "ID": 2,
#     "Student": {
#       "Name": "Zara",
#       "Details": {"Age": 21, "City": "Islamabad"}
#     }
#   }
# ]
# import json
# import pandas as pd
# with open('deep_nested.json') as f:
#     data = json.load(f)
# df = pd.json_normalize(data, record_path=None)
# print(df)









# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, 30, 22, 28],
#     "Marks": [85, 90, 95, 88]
# }
# df = pd.DataFrame(data)
# print(df)

# # df.describe() → Numerical stats summary

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, 30, 22, 28],
#     "Marks": [85, 90, 95, 88]
# }
# df = pd.DataFrame(data)
# print(df.describe())

# # df["Marks"].mean() → Mean of column

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, 30, 22, 28],
#     "Marks": [85, 90, 95, 88]
# }
# df = pd.DataFrame(data)
# print(df["Marks"].mean())  

# # More Functions

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, 30, 22, 28],
#     "Marks": [85, 90, 95, 88]
# }
# df = pd.DataFrame(data)
# df["Marks"].max()      
# df["Marks"].min()     
# df["Marks"].sum()      
# df["Marks"].median()   
# df["Marks"].std()      

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, 30, 22, 28],
#     "Marks": [85, 90, 95, 88]
# }
# df = pd.DataFrame(data)
# print(df["Age"].value_counts())







# df.isnull() & df.notnull()

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", None],
#     "Age": [25, None, 22, 30],
#     "City": ["Lahore", "Karachi", None, "Islamabad"]
# }
# df = pd.DataFrame(data)
# print(df.isnull())     
# print(df.notnull())     

# # Remove Rows with Any Missing Data

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", None],
#     "Age": [25, None, 22, 30]
# }
# df = pd.DataFrame(data)
# clean_df = df.dropna()
# print(clean_df)

# # Fill Missing Values with Default

# import pandas as pd

# data = {
#     "Name": ["Ali", "Ahmed", None],
#     "City": ["Lahore", None, "Karachi"]
# }
# df = pd.DataFrame(data)
# df_filled = df.fillna("Unknown")
# print(df_filled)








# # Remove Rows with Empty Cells

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, None, 22, 30]
# }
# df = pd.DataFrame(data)
# df.dropna(inplace=True)
# print(df)

# # Fill Empty Cells with Specific Value

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, None, 22, 30]
# }
# df = pd.DataFrame(data)
# df.fillna("Unknown", inplace=True)

# # Fill with Mean / Median / Mode (numerical columns)

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, None, 22, 30]
# }
# df = pd.DataFrame(data)
# df["Age"].fillna(df["Age"].mean(), inplace=True)   
# # df["Age"].fillna(df["Age"].median(), inplace=True)  
# # df["Age"].fillna(df["Age"].mode()[0], inplace=True)  
# print(df)

# # Another Example

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, None, 22, 30]
# }
# df = pd.DataFrame(data)
# df["Age"].fillna(df["Age"].mean(), inplace=True)
# print(df)







# # Visualize the example

# import pandas as pd
# data = {
#     "Date": ["2024-01-01", "01-02-2024", "bad_date"],
#     "Price": ["100", "200", "two hundred"]
# }
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
# df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
# print(df)

# # Cleaning Currency Strings

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara"],
#     "Amount": ["Rs 1000", "Rs  2500 ", "Rs3000"]
# }
# df = pd.DataFrame(data)
# df["Amount"] = df["Amount"].str.replace("Rs", "").str.strip()
# df["Amount"] = pd.to_numeric(df["Amount"])
# print(df)
# # Remove Commas from Numbers

# import pandas as pd

# data = {
#     "Salary": ["10,000", "25,000", "30,500"]
# }

# df = pd.DataFrame(data)
# df["Salary"] = df["Salary"].str.replace(",", "")
# df["Salary"] = pd.to_numeric(df["Salary"])
# print(df)

# # Convert Dates to Proper Format

# import pandas as pd
# data = {
#     "JoinDate": ["2024-01-01", "12-05-2024", "13/05/2024", "Invalid"]
# }
# df = pd.DataFrame(data)
# df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors='coerce')
# print(df)

# # Remove % Symbol and Convert

# import pandas as pd
# data = {
#     "Growth": ["10%", "15%", "7.5%", "12%"]
# }
# df = pd.DataFrame(data)
# df["Growth"] = df["Growth"].str.replace("%", "")
# df["Growth"] = pd.to_numeric(df["Growth"])
# print(df)











# # Visulaize the example

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Zara", "Usman"],
#     "Age": [25, -3, 130, 28],
#     "Marks": [88, 105, 92, 80]
# }
# df = pd.DataFrame(data)
# df = df[(df["Age"] >= 0) & (df["Age"] <= 100)]
# df.loc[df["Marks"] > 100, "Marks"] = 100
# print(df)

# # Replace Negative Values with Median

# import pandas as pd
# data = {
#     "Product": ["A", "B", "C", "D"],
#     "Quantity": [10, -5, 20, -2]
# }
# df = pd.DataFrame(data)
# median_qty = df[df["Quantity"] >= 0]["Quantity"].median()
# df.loc[df["Quantity"] < 0, "Quantity"] = median_qty
# print(df)

# # Remove Nonsense Names

# import pandas as pd
# data = {
#     "Name": ["Ali", "1234", "Ahmed", "???"],
#     "Age": [25, 30, 22, 28]
# }

# df = pd.DataFrame(data)
# df = df[df["Name"].str.isalpha()]
# print(df)









# # Visualize the example

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ahmed", "Ali", "Zara", "Ahmed"],
#     "Age": [25, 30, 25, 22, 30]
# }
# df = pd.DataFrame(data)
# df.drop_duplicates(inplace=True)
# print(df)

# # Detect & Count Duplicate Rows

# import pandas as pd
# data = {
#     "Name": ["Ali", "Ali", "Zara", "Zara", "Usman"],
#     "Age": [25, 25, 22, 22, 30]
# }
# df = pd.DataFrame(data)
# print(df.duplicated())
# print("Duplicates found:", df.duplicated().sum())

# # Keep Only Last Occurrence

# import pandas as pd
# df = pd.DataFrame({
#     "Email": ["a@example.com", "b@example.com", "a@example.com"]
# })
# df = df.drop_duplicates(keep="last")
# print(df)

# # Drop Duplicates Based on One Column Only

# import pandas as pd
# df = pd.DataFrame({
#     "ID": [1, 2, 3, 4],
#     "Name": ["Ali", "Ali", "Zara", "Zara"],
#     "Marks": [80, 90, 85, 85]
# })
# df = df.drop_duplicates(subset=["Name"])
# print(df)












# # df.corr() → Correlation Matrix

# import pandas as pd
# data = {
#     "Math": [80, 85, 78, 90],
#     "Physics": [75, 88, 70, 95],
#     "English": [60, 55, 65, 58]
# }
# df = pd.DataFrame(data)
# print(df.corr())

# # Positive Correlation

# import pandas as pd
# data = {
#     "Hours_Studied": [1, 2, 3, 4, 5],
#     "Marks": [50, 60, 65, 70, 80]
# }
# df = pd.DataFrame(data)
# print(df.corr())

# # Negative Correlation

# import pandas as pd
# data = {
#     "Age": [18, 25, 35, 45, 60],
#     "Running_Speed": [20, 18, 15, 12, 8]
# }
# df = pd.DataFrame(data)
# print(df.corr())

# # No Correlation

# import pandas as pd
# data = {
#     "Temperature": [30, 25, 20, 15, 10],
#     "Phone_Calls": [50, 51, 49, 48, 50]
# }
# df = pd.DataFrame(data)
# print(df.corr())








# Visualize the code

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# data = {
#     "Math": [80, 85, 78, 90],
#     "Physics": [75, 88, 70, 95],
#     "English": [60, 55, 65, 58]
# }
# df = pd.DataFrame(data)
# corr = df.corr()
# sns.heatmap(corr, annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()

# Correlation Heatmap with Customizations

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# data = {
#     "Height": [170, 165, 180, 175, 160],
#     "Weight": [65, 55, 75, 70, 50],
#     "Age": [30, 25, 35, 40, 28]
# }
# df = pd.DataFrame(data)
# corr = df.corr()
# plt.figure(figsize=(6, 4))
# sns.heatmap(corr, annot=True, cmap="YlGnBu", linewidths=0.5)
# plt.title("Correlation Heatmap with Custom Style")
# plt.show()

# Pairplot for Correlation Exploration

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# data = {
#     "SepalLength": [5.1, 4.9, 4.7, 4.6, 5.0],
#     "SepalWidth": [3.5, 3.0, 3.2, 3.1, 3.6],
#     "PetalLength": [1.4, 1.4, 1.3, 1.5, 1.4],
#     "PetalWidth": [0.2, 0.2, 0.2, 0.2, 0.2]
# }
# df = pd.DataFrame(data)
# sns.pairplot(df)
# plt.show()







# # Visualize the code

# import pandas as pd
# import matplotlib.pyplot as plt
# data = {
#     "Year": [2018, 2019, 2020, 2021],
#     "Sales": [200, 250, 300, 400],
#     "Profit": [20, 30, 50, 70]
# }
# df = pd.DataFrame(data)
# df.plot(x="Year", y="Sales")
# plt.show()
# df.plot(kind="bar", x="Year", y="Profit")
# plt.show()
# df.plot(kind="scatter", x="Sales", y="Profit")
# plt.show()

# # Histogram Plot (Distribution Check)

# import pandas as pd
# import matplotlib.pyplot as plt
# data = {
#     "Age": [23, 45, 56, 23, 44, 55, 67, 34, 45, 33, 25, 36, 40]
# }
# df = pd.DataFrame(data)
# df["Age"].plot(kind="hist", bins=5, color="skyblue", edgecolor="black")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# # Box Plot (Summary & Outlier Detection)

# import pandas as pd
# import matplotlib.pyplot as plt
# data = {
#     "Salary": [30000, 35000, 40000, 45000, 1000000, 38000, 42000, 39000]
# }
# df = pd.DataFrame(data)
# df["Salary"].plot(kind="box")
# plt.title("Salary Distribution and Outliers")
# plt.show()
