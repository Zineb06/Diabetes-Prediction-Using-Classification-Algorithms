import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder

data = pd.read_csv('dataset/diabetes-1.csv')

data.info()
data.head()
data.describe()

print(data.isnull().sum())  # Check for missing values
data = data.dropna()  # Drop rows with missing values


# scaler = StandardScaler()
# data[['numerical_column1', 'numerical_column2']] = scaler.fit_transform(data[['numerical_column1', 'numerical_column2']])

sns.pairplot(data)
plt.show()
