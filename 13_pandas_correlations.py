#Visualize the code

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Math": [80, 85, 78, 90],
    "Physics": [75, 88, 70, 95],
    "English": [60, 55, 65, 58]
}
df = pd.DataFrame(data)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#Correlation Heatmap with Customizations

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Height": [170, 165, 180, 175, 160],
    "Weight": [65, 55, 75, 70, 50],
    "Age": [30, 25, 35, 40, 28]
}
df = pd.DataFrame(data)
corr = df.corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Correlation Heatmap with Custom Style")
plt.show()

#Pairplot for Correlation Exploration

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data = {
    "SepalLength": [5.1, 4.9, 4.7, 4.6, 5.0],
    "SepalWidth": [3.5, 3.0, 3.2, 3.1, 3.6],
    "PetalLength": [1.4, 1.4, 1.3, 1.5, 1.4],
    "PetalWidth": [0.2, 0.2, 0.2, 0.2, 0.2]
}
df = pd.DataFrame(data)
sns.pairplot(df)
plt.show()
