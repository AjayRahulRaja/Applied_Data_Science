import pandas as pd

df = pd.read_excel("C://Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj 02/API_19_DS2_en_excel_v2_4903056.xls", header=3)
print(df.head(2))

df=df.drop(['Country Code', 'Indicator Code'], axis=1)
df.set_index(['Country Name', 'Indicator Name'], inplace=True)
df.sort_index(inplace=True)                # sort index
print(df.head(3))

df=df.T
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(df.head(4))


