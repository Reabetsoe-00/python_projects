
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set seaborn style
sns.set(style='whitegrid')

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Display the first few rows
print("\nFirst 5 Rows:")
print(df.head())

# Explore the structure of the dataset
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())

# Clean dataset (drop missing values if any)
df = df.dropna()

# Basic Statistics
print("\nBasic Statistics:")
print(df.describe())

# Grouping by species and calculating mean
grouped = df.groupby('species').mean()
print("\nMean values grouped by species:")
print(grouped)

# Visualization 1: Line Chart
plt.figure(figsize=(8, 5))
for species in df['species'].unique():
    species_data = df[df['species'] == species].reset_index()
    plt.plot(species_data.index, species_data['sepal length (cm)'], label=species)

plt.title("Sepal Length Trend by Species")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.tight_layout()
plt.savefig("line_chart_sepal_length.png")
plt.show()

# Visualization 2: Bar Chart
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='species', y='petal length (cm)', ci=None)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig("bar_chart_petal_length.png")
plt.show()

# Visualization 3: Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['sepal width (cm)'], bins=15, kde=True, color='skyblue')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_sepal_width.png")
plt.show()

# Visualization 4: Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.tight_layout()
plt.savefig("scatter_sepal_petal_length.png")
plt.show()
