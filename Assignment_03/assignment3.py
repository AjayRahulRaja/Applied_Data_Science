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
    
    test_df = df.copy()
    # extract the country names
    countries = test_df['Country Name'].unique()
    # keep only the indicator and values
    new_df = test_df.loc[:, test_df.columns.isin(['Indicator Name',
                                                  str(year)])]

    f_len = len(fields) - 1
    
    # column headers for resulting data frame
    col_list = ['Country'] + fields

    # empty data frame for resulting data frame
    mod_df = pd.DataFrame(columns=col_list)
    
    # process to create the resulting df
    for i in range(len(countries)):
        start = i + i*f_len # start position to slice
        end = i + i*f_len + f_len + 1 # end pos to slice
        temp = new_df[start:end].T # transpose the data
        temp.reset_index(inplace=True) # reset the index
        temp.columns = temp.iloc[0] # set the first row to column header
        temp = temp.iloc[1:] # delete the first row
        temp.rename(columns={'Indicator Name': 'Country'}, inplace=True)
        temp.loc[1, 'Country'] = countries[i] # set the country name
        mod_df = pd.concat([mod_df, temp], axis=0, ignore_index=True) # concate the current DF with existing DF

    return mod_df

# main code
df = pd.read_excel("API_19_DS2_en_excel_v2_4903056.xls", header=3)
#Discovering data using .describe()
df.describe()
#Redundant Columns to be removed
removeColumns=['Country Code', 'Indicator Code']


new_df = transformDf(df, removeColumns)

year = 2016

# fields to be filtered
fields = ['Population, total',
      'Agricultural land (sq. km)',
      'Arable land (% of land area)',
      'Forest area (sq. km)',
      'Cereal yield (kg per hectare)',
      'CO2 emissions (kg per PPP $ of GDP)',
      'CO2 emissions (kt)',
      'CO2 emissions from gaseous fuel consumption (kt)',
      'CO2 emissions from solid fuel consumption (kt)',
      'CO2 emissions from liquid fuel consumption (kt)']

# filter the dataframe with fields and year
mod_df = filterFieldsAndYear(new_df, fields, year)

hm_df = transformDf2(mod_df)

hm_df['Population, total'] = hm_df['Population, total'].astype('float64')
hm_df['Agricultural land (sq. km)'] = hm_df['Agricultural land (sq. km)'].astype('float64')
hm_df['Arable land (% of land area)'] = hm_df['Arable land (% of land area)'].astype('float64')
hm_df['Forest area (sq. km)'] = hm_df['Forest area (sq. km)'].astype('float64')
hm_df['Cereal yield (kg per hectare)'] = hm_df['Cereal yield (kg per hectare)'].astype('float64')
hm_df['CO2 emissions (kg per PPP $ of GDP)'] = hm_df['CO2 emissions (kg per PPP $ of GDP)'].astype('float64')
hm_df['CO2 emissions (kt)'] = hm_df['CO2 emissions (kt)'].astype('float64')
hm_df['CO2 emissions from gaseous fuel consumption (kt)'] = hm_df['CO2 emissions from gaseous fuel consumption (kt)'].astype('float64')
hm_df['CO2 emissions from solid fuel consumption (kt)'] = hm_df['CO2 emissions from solid fuel consumption (kt)'].astype('float64')
hm_df['CO2 emissions from liquid fuel consumption (kt)'] = hm_df['CO2 emissions from liquid fuel consumption (kt)'].astype('float64')



# heat map for the world data
plt.figure()
ct.map_corr(hm_df)
plt.title('Heatmap')
plt.show()

# scatter matrix
plt.figure(dpi=600)
pd.plotting.scatter_matrix(hm_df, figsize=(9.0, 9.0))
plt.tight_layout()    # helps to avoid overlap of labels
plt.show()
