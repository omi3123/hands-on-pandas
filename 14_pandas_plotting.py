# Visualize the code

import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Year": [2018, 2019, 2020, 2021],
    "Sales": [200, 250, 300, 400],
    "Profit": [20, 30, 50, 70]
}
df = pd.DataFrame(data)
df.plot(x="Year", y="Sales")
plt.show()
df.plot(kind="bar", x="Year", y="Profit")
plt.show()
df.plot(kind="scatter", x="Sales", y="Profit")
plt.show()

# Histogram Plot (Distribution Check)

import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Age": [23, 45, 56, 23, 44, 55, 67, 34, 45, 33, 25, 36, 40]
}
df = pd.DataFrame(data)
df["Age"].plot(kind="hist", bins=5, color="skyblue", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Box Plot (Summary & Outlier Detection)

import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Salary": [30000, 35000, 40000, 45000, 1000000, 38000, 42000, 39000]
}
df = pd.DataFrame(data)
df["Salary"].plot(kind="box")
plt.title("Salary Distribution and Outliers")
plt.show()
