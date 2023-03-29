"""
Module to read the source data and has the functions to transpose and clean data.
Custom functions have been implemented to create custom colors for heatmaps.
Also calculates the normalised skewness

@author: ajay rahul
"""

""" Module to provide five functions:
    Cleans the input DataFrame
    Transposes a input DataFrame, converting columns to rows 
    Filtering DataFrame for analysis
    Creating custom colors for heatmap
    Generating DataFrame for energy consumptions
"""
#importing module and library
import pandas as pd
import stats

#Reading Source Data
df = pd.read_excel("C://Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj 02/API_19_DS2_en_excel_v2_4903056.xls", header=3)
#Discovering data using .describe()
df.describe()
#Redundant Columns to be removed
removeColumns=['Country Code', 'Indicator Code']
indexColumns=["Country Name", "Indicator Name"]

def transformDf(df, removeColumns, indexColumns):
    """
    This Function takes input file as DataFrame and removes redundant columns
    :param df: CSV file as a DataFrame type
    :param removeColumns: Columns need to be removed form the DataFrame
    :param indexColumns: Columns need to be set as Index for slicing
    :return: Cleaned DataFrame with Years as Columns and Index are set with Country Name and Indicator Name columns
    """
    df=df.drop(removeColumns, axis=1)
    df.set_index(indexColumns, inplace=True)
    df.sort_index(inplace=True)
    return df
new_df = transformDf(df, removeColumns, indexColumns)
new_df.describe()
def transformDf2(df):
    """
    This Function takes the cleaned DataFrame and will Transpose it. Also All NaN values will be filled with 0s.
    :param df: Cleaned DataFrame with Years as Columns
    :return: DataFrame with Country Names as Columns
    """
    df.fillna(0)
    df=df.T
    return df
new_df1=transformDf2(new_df)
new_df1.describe()
#Creating list of countires to be filtered
countryList=['France', 'United Kingdom', 'India', 'Japan', 'Cuba', 'Colombia', 'Iraq', 'Algeria', 'Australia']
def fillterCountries(df):
    """
    This function takes the Transposed DataFrame and iterate over the list of selected countries to get filter the DataFrame
    :param df: Transposed DataFrame
    :return: DataFrame of all Selected countries' data
    """
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
    """
    This function takes three parameters in order to get the RGB value of a country's flag.
    :param r: Red Color Value
    :param g: Green Color Value
    :param b: Blue Color Value
    :return: list of RGB values
    """
    return [r/256, g/256, b/256]
def getPowerConsumption(df, column, years):
    """
    This function takes the transposed DataFrame and provides a table of country names and its energy consumption for a few years
    :param df: Input transposed DataFrame
    :param column: Electric power consumption (kWh per capita) column
    :param years: Following years in List 1960, 1990, 2020
    :return: DataFrame of countries and it's energy consumption for three years
    """
    d = {}
    for x in countryList:
        d[x] = df.loc[(years), (x, column)]
    return d

#Finding the skewness for France's indicators
France_skew = stats.skew(France)
France_skew = pd.DataFrame(France_skew)
France_skew = France_skew.loc[('Renewable energy consumption (% of total final energy consumption)', 'Total greenhouse gas emissions (% change from 1990)', 'Other greenhouse gas emissions, HFC, PFC and SF6 (thousand metric tons of CO2 equivalent)', 'Methane emissions (% change from 1990)'), :]
France_skew = France_skew.rename(columns = {0:"France"})
France_skew = France_skew.T
#Finding the skewness for Iraq's indicators
Iraq_skew = stats.skew(Iraq)
Iraq_skew = pd.DataFrame(Iraq_skew)
Iraq_skew = Iraq_skew.loc[('Renewable energy consumption (% of total final energy consumption)', 'Total greenhouse gas emissions (% change from 1990)', 'Other greenhouse gas emissions, HFC, PFC and SF6 (thousand metric tons of CO2 equivalent)', 'Methane emissions (% change from 1990)'), :]
Iraq_skew = Iraq_skew.rename(columns = {0:"Iraq"})
Iraq_skew = Iraq_skew.T
#Finding the skewness for Japan's indicators
Japan_skew = stats.skew(Japan)
Japan_skew = pd.DataFrame(Japan_skew)
Japan_skew = Japan_skew.loc[('Renewable energy consumption (% of total final energy consumption)', 'Total greenhouse gas emissions (% change from 1990)', 'Other greenhouse gas emissions, HFC, PFC and SF6 (thousand metric tons of CO2 equivalent)', 'Methane emissions (% change from 1990)'), :]
Japan_skew = Japan_skew.rename(columns = {0:"Japan"})
Japan_skew = Japan_skew.T
#Combaining France, Iraq, Japan's skew into a dataframe
all_skew = pd.concat([France_skew, Iraq_skew, Japan_skew])

all_skew = all_skew.rename(columns = {'Renewable energy consumption (% of total final energy consumption)':"Renewable energy consumption",
                                      'Total greenhouse gas emissions (% change from 1990)':'Total greenhouse gas emissions',
                                      'Other greenhouse gas emissions, HFC, PFC and SF6 (thousand metric tons of CO2 equivalent)':'Other greenhouse gas emissions',
                                      'Methane emissions (% change from 1990)':'Methane emissions'
                                      }
                           )
all_skew=all_skew.T
print(all_skew)
