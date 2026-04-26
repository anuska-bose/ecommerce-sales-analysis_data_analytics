import pandas as pd

df = pd.read_csv("ecommerce_sales_data.csv")

print(df.head())

print(df.info())
print(df.describe())
print(df.columns)

df = df.drop_duplicates()

print(df.isnull().sum())

df = df.dropna()   # OR fill values

df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")

df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Ad_Spend'] = pd.to_numeric(df['Ad_Spend'], errors='coerce')

month_map = {
    'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4,
    'May':5, 'Jun':6, 'Jul':7, 'Aug':8,
    'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12
}

df['Month_Number'] = df['Month'].map(month_map)

df['Profit_Margin'] = df['Profit'] / df['Revenue']

# Revenue by Region
print(df.groupby('Region')['Revenue'].sum())

# Profit by Category
print(df.groupby('Category')['Profit'].sum())

df.to_excel("cleaned_data.xlsx", index=False)

month_map = {
    'January':1, 'February':2, 'March':3, 'April':4,
    'May':5, 'June':6, 'July':7, 'August':8,
    'September':9, 'October':10, 'November':11, 'December':12
}
df['Month_Number'] = df['Month'].map(month_map)
print(df[['Month', 'Month_Number']].head())
print(df['Month_Number'].unique())
df.to_excel("cleaned_data.xlsx", index=False)
df.to_csv("cleaned_data.csv", index=False)
print("File saved successfully!")
df = pd.read_csv("ecommerce_sales_data_cleaned.xlsx")
df.to_csv("cleaned_data.csv", index=False)