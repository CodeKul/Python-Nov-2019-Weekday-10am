import pandas as pd   # pip install pandas

sr = pd.Series([1,2,3,4,5,6,7,8,9], ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'])
print(sr)
print(type(sr.values))
print(sr.values)
print(sr.sort_values(ascending=False))
print(sr.sort_index())

df1 = pd.DataFrame({'Python': [12, 43, 54, 16, 63], 'C': [32, 56, 23, 67, 21], 'Java': [23, 56, 63, 45, 52]}, ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(df1)
df2 = pd.DataFrame({'Kotlin': [12, 43, 54, 16, 63], 'Swift': [32, 56, 23, 67, 21], 'C++': [23, 56, 63, 45, 52]}, ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(df2)

# Operations

df3 = pd.concat([df1, df2])
print(df3)

df = pd.read_csv('dataset.csv')
print(df)

df.info(null_counts=True)

# - Analysis Operations
print(df.head(3))
print(df.tail(3))
print(df.shape)

print(df.Cost.describe())
print(df.describe())


# - Data cleaning

df.rename(columns={'Index': 'index'}, inplace=True)
print(df)

df.Cost = df.Cost.fillna(df.Total-df.Tax)

df = df.drop(columns=['index'])
print(df)

df_corr = df[['Item', 'Cost', 'Tax']].corr()
print(df_corr)

df['Cost'] = df.Cost.astype(object) 
print(df.info())