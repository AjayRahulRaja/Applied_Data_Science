import pandas as pd

df = pd.read_excel("C://Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj 02/API_19_DS2_en_excel_v2_4903056.xls", header=3)

removeColumns=['Country Code', 'Indicator Code']
indexColumns=["Country Name", "Indicator Name"]

def transformDf(df, removeColumns, indexColumns):
    df=df.drop(removeColumns, axis=1)
    df.set_index(indexColumns, inplace=True)
    df.sort_index(inplace=True)
    return df

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
new_df=transformDf(df, removeColumns, indexColumns)
new_df.head(2)

def transformDf2(df):
    df.fillna(0)
    df=df.T
    return df

new_df1=transformDf2(new_df)
new_df1.head(2)

countryList=['France', 'United Kingdom', 'India', 'Japan', 'Cuba', 'Colombia', 'Iraq', 'Algeria', 'Australia']
def fillterCountries(df):
    d={}
    for x in countryList:
        d[x] = df.loc[:, x]
    return d

x=fillterCountries(new_df1)
France, United_Kingdom, India, Japan, Cuba, Colombia, Iraq, Algeria, Australia=x['France'], x['United Kingdom'], x['India'], x['Japan'], x['Cuba'], x['Colombia'], x['Iraq'], x['Algeria'], x['Australia']