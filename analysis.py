import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (same folder)
df = pd.read_csv('sales.csv')

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Analysis
sales_by_region = df.groupby('Region')['Sales'].sum()
profit_by_category = df.groupby('Category')['Profit'].sum()

# Print insights
print("Top Region:", sales_by_region.idxmax())
print("Best Category:", profit_by_category.idxmax())

# Plot
sales_by_region.plot(kind='bar', title='Sales by Region')
plt.show()
