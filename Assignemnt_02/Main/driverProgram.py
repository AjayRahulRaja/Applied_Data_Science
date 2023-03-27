import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

#Reading Source Data
df = pd.read_excel("C://Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj 02/API_19_DS2_en_excel_v2_4903056.xls", header=3)
df.describe()

#Redundant Columns to be removed
removeColumns=['Country Code', 'Indicator Code']
indexColumns=["Country Name", "Indicator Name"]

def transformDf(df, removeColumns, indexColumns):
    '''
    This Function takes input file as DataFrame and removes redundant columns
    :param df: CSV file as a DataFrame type
    :param removeColumns: Columns need to be removed form the DataFrame
    :param indexColumns: Columns need to be set as Index for slicing
    :return: Cleaned DataFrame with Years as Columns and Index are set with Country Name and Indicator Name columns
    '''
    df=df.drop(removeColumns, axis=1)
    df.set_index(indexColumns, inplace=True)
    df.sort_index(inplace=True)
    return df
new_df = transformDf(df, removeColumns, indexColumns)
new_df.describe()

def transformDf2(df):
    '''
    This Function takes the cleaned DataFrame and will Transpose it. Also All NaN values will be filled with 0s.
    :param df: Cleaned DataFrame with Years as Columns
    :return: DataFrame with Country Names as Columns
    '''
    df.fillna(0)
    df=df.T
    return df
new_df1=transformDf2(new_df)
new_df1.describe()

countryList=['France', 'United Kingdom', 'India', 'Japan', 'Cuba', 'Colombia', 'Iraq', 'Algeria', 'Australia']
def fillterCountries(df):
    '''
    This function takes the Transposed DataFrame and iterate over the list of selected countries to get filter the DataFrame
    :param df: Transposed DataFrame
    :return: DataFrame of all Selected countries' data
    '''
    d={}
    for x in countryList:
        d[x] = df.loc[:, x]
    return d

#saving the filtered data
x=fillterCountries(new_df1)
#assinging each countries' data to its variable
France, United_Kingdom, India, Japan, Cuba, Colombia, Iraq, Algeria, Australia = x['France'], \
                                                                                 x['United Kingdom'], \
                                                                                 x['India'], \
                                                                                 x['Japan'], \
                                                                                 x['Cuba'], \
                                                                                 x['Colombia'], \
                                                                                 x['Iraq'], \
                                                                                 x['Algeria'], \
                                                                                 x['Australia']

def create_color(r, g, b):
    '''
    This function takes three parameters in order to get the RGB value of a country's flag.
    :param r: Red Color Value
    :param g: Green Color Value
    :param b: Blue Color Value
    :return: list of RGB values
    '''
    return [r/256, g/256, b/256]

def getPowerConsumption(df, column, years):
    '''
    This function takes the transposed DataFrame and provides a table of country names and its energy consumption for a few years
    :param df: Input transposed DataFrame
    :param column: Electric power consumption (kWh per capita) column
    :param years: Following years in List 1960, 1990, 2020
    :return: DataFrame of countries and it's energy consumption for three years
    '''
    d = {}
    for x in countryList:
        d[x] = df.loc[(years), (x, column)]
    return d

