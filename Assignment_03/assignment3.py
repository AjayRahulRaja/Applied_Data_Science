"""

@author: ajay rahul
"""

import pandas as pd
import stats
import matplotlib.pyplot as plt
import stats
import cluster_tools as ct
import sklearn.cluster as cluster
import sklearn.metrics as skmet


def transformDf(df, removeColumns):
    """
    This Function takes input file as DataFrame and removes redundant columns
    :param df: CSV file as a DataFrame type
    :param removeColumns: Columns need to be removed form the DataFrame
    :param indexColumns: Columns need to be set as Index for slicing
    :return: Cleaned DataFrame with Years as Columns and Index are set with Country Name and Indicator Name columns
    """
    df=df.drop(removeColumns, axis=1)
    df.sort_index(inplace=True)
    df.fillna(0, inplace=True)
    return df


def filterFieldsAndYear(df, fields, year):
    """
    This function keeps only required fields for further processing
    :param df: Transposed DataFrame
    :return: DataFrame of all Selected countries' data
    """
    new_df = df.loc[df['Indicator Name'].isin(fields)]
    sliced_df = new_df.loc[:, new_df.columns.isin(['Country Name', 'Indicator Name', str(year)])]
    sliced_df.sort_index(inplace=True)
    return sliced_df


def transformDf2(df):
    """
    This Function takes the cleaned DataFrame and will Transpose it. Also All NaN values will be filled with 0s.
    :param df: Cleaned DataFrame with Years as Columns
    :return: DataFrame with Country Names as Columns
    """
    
    countries = df['Country Name'].unique()
    return df


df = pd.read_excel("API_19_DS2_en_excel_v2_4903056.xls", header=3)
#Discovering data using .describe()
df.describe()
#Redundant Columns to be removed
removeColumns=['Country Code', 'Indicator Code']


new_df = transformDf(df, removeColumns)


year = 2017

# fields to be filtered
fields = ['Population growth (annual %)',
      'Agricultural land (% of land area)',
      'Arable land (% of land area)',
      'Forest area (% of land area)',
      'Cereal yield (kg per hectare)',
      'CO2 emissions (kg per PPP $ of GDP)',
      'CO2 emissions (kt)',
      'CO2 emissions from gaseous fuel consumption (% of total)',
      'CO2 emissions from solid fuel consumption (% of total)',
      'CO2 emissions from liquid fuel consumption (% of total)']

# filter the dataframe with fields and year
mod_df = filterFieldsAndYear(new_df, fields, year)

# to copy the df
tdf = mod_df.copy()
# extract the country names
countries = tdf['Country Name'].unique()
# keep only the indicator and values
new_df = tdf.loc[:, tdf.columns.isin(['Indicator Name', str(year)])]

f_len = len(fields) - 1
# i = 0

col_list = ['Country'] + fields
mod_df = pd.DataFrame(columns=col_list)


for i in range(len(countries)):
    start = i + i*f_len # start position to slice
    end = i + i*f_len + f_len # end pos to slice
    temp = new_df[start:end].T # transpose the data
    temp.columns = temp.iloc[0] # set the first row to column header
    temp = temp.iloc[1:] # delete the first row
    temp.reset_index(inplace=True) # reset the index
    temp.loc[0, 'index'] = countries[i] # set the country name
    
    
    

a = new_df[0:9].T
a.reset_index(inplace=True)
a.columns=a.iloc[0]
c = a.iloc[1:]
c.rename(columns={'Indicator Name': 'Country'}, inplace=True)
c.loc[1, 'Country'] = 'UK'

display(c)

vertical_concat = pd.concat([mod_df, c], axis=0)






# b = c.to_dict('r')
# d = b[0]
# d.pop('Indicator Name')
# e = {'Country':'dummy'}
# f = e | d
# g = 
# mod_df = (f, ignore_index=True)

b = new_df[10:19].T
    






