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

# - Manipulating/Indexing/sorting dataset

print(df.iloc[2:5,:])

print(df.iloc[0:3, 2])
# df.iloc[:,:]
print(df.iloc[6:, 2:])
# df.iloc[:, 1]

print(df.loc[:, 'Cost'])
print(df.loc[:6, 'Item'])
print(df.loc[:6, 'Item':'Tax'])
df['Tax'] = 1	#sets value 1 to entire column
print(df)

# applying lambda functions:
f = lambda x: x*2
df['Tax'] = df['Tax'].apply(f)
print(df)

# sorting:
print(df.sort_values(by='Cost', ascending=True))

# Filtering:
# df['Cost'] > 6	# will get True False values for every row in column1 which are greater than 6

filter1 = df['Cost'] > 6
filtered_df = df[filter1]

filter2 = (df['Cost'] > 6) & (df['Cost'] < 10)
filtered_df = df[filter2]
print(filtered_df)


# https://www.analyticsvidhya.com/blog/2018/05/24-ultimate-data-science-projects-to-boost-your-knowledge-and-skills/