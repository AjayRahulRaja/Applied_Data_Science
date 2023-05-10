"""

@author: ajay rahul
"""

#importing module and library
import pandas as pd
import stats
import matplotlib.pyplot as plt
import stats
import cluster_tools as ct
import sklearn.cluster as cluster
import sklearn.metrics as skmet
from matplotlib.colors import LinearSegmentedColormap


#Creating list of countires to be filtered
countryList=['France', 'United Kingdom', 'India', 'Japan', 'Cuba', 'Colombia', 'Iraq', 'Algeria', 'Australia']


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


def transformDf2(df):
    """
    This Function takes the cleaned DataFrame and will Transpose it. Also All NaN values will be filled with 0s.
    :param df: Cleaned DataFrame with Years as Columns
    :return: DataFrame with Country Names as Columns
    """
    df.fillna(0)
    df=df.T
    return df


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


def get_custom_color_palette():
     return LinearSegmentedColormap.from_list("", [
          create_color(0,85,164), 
          create_color(255,255,255), 
          create_color(239,65,53)
     ])


#Reading Source Data
df = pd.read_excel("API_19_DS2_en_excel_v2_4903056.xls", header=3)
#Discovering data using .describe()
df.describe()
#Redundant Columns to be removed
removeColumns=['Country Code', 'Indicator Code']
indexColumns=["Country Name", "Indicator Name"]


new_df = transformDf(df, removeColumns, indexColumns)
new_df.describe()


#transpose the data frame
new_df1=transformDf2(new_df)
new_df1.describe()

#saving the filtered data
x = fillterCountries(new_df1)

#assinging each countries' data to its variable
France, United_Kingdom, India  = x['France'], x['United Kingdom'], x['India']
Japan, Cuba, Colombia= x['Japan'], x['Cuba'], x['Colombia']
Iraq, Algeria, Australia = x['Iraq'], x['Algeria'], x['Australia']


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
#Renaming column names
all_skew = all_skew.rename(columns = {'Renewable energy consumption (% of total final energy consumption)':"Renewable energy consumption",
                                      'Total greenhouse gas emissions (% change from 1990)':'Total greenhouse gas emissions',
                                      'Other greenhouse gas emissions, HFC, PFC and SF6 (thousand metric tons of CO2 equivalent)':'Other greenhouse gas emissions',
                                      'Methane emissions (% change from 1990)':'Methane emissions'
                                      }
                           )
all_skew=all_skew.T
print(all_skew)

#Output of Skewness for France, Iraq, and Japan
#                                 France    Iraq      Japan
# Indicator Name
# Renewable energy consumption    0.346325  0.570013  0.663760
# Total greenhouse gas emissions -0.324172 -0.119706 -0.182678
# Other greenhouse gas emissions  0.071156 -0.326243 -0.174798
# Methane emissions              -0.266908 -0.214166  0.236731



#importing module and library



France.describe()
#Filtering and saving France's different years and different parameter.
heat_map_parameters = ['Population growth (annual %)',
      'Agricultural land (% of land area)',
      'Arable land (% of land area)',
      'Forest area (% of land area)',
      'Cereal yield (kg per hectare)',
      'CO2 emissions (kg per PPP $ of GDP)',
      'CO2 emissions (kt)',
      'CO2 emissions from gaseous fuel consumption (% of total)',
      'CO2 emissions from solid fuel consumption (% of total)',
      'CO2 emissions from liquid fuel consumption (% of total)']

Fr_df = France.loc[:, France.columns.isin(heat_map_parameters)]
Fr_df.fillna(0, inplace=True)

#calculating correlation for France
corr_france_heat_map = Fr_df.corr()
print(corr_france_heat_map)
#getting France flag color for heat map custom color

#plotting heat map
plt.figure(figsize=(8, 6))
#sns.heatmap(corr_france_heat_map, cmap=cmap, annot=True, linewidths=0.5, annot_kws={'size': 10})
ct.map_corr(Fr_df)
plt.title('France')
# plt.savefig('C:/Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj 02/plots/New folder/fra_heat_map_dpi.png',
#             dpi=400,
#             bbox_inches ="tight",
#             pad_inches = 1,
#             transparent = False,
#             orientation ='landscape')
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()

plt.figure(dpi=600)
pd.plotting.scatter_matrix(Fr_df, figsize=(9.0, 9.0))
plt.tight_layout()    # helps to avoid overlap of labels
plt.show()

###########finding n clusters
# extract columns for fitting. 
fr_df_fit = Fr_df[['Population growth (annual %)', 'Cereal yield (kg per hectare)']].copy()

# normalise dataframe and inspect result
# normalisation is done only on the extract columns. .copy() prevents
# changes in df_fit to affect df_fish. This make the plots with the 
# original measurements
fr_df_fit, df_min, df_max = ct.scaler(fr_df_fit)
print(fr_df_fit.describe())
print()

print("n   score")
# loop over trial numbers of clusters calculating the silhouette
for ic in range(2, 7):
    # set up kmeans and fit
    kmeans = cluster.KMeans(n_clusters=ic)
    kmeans.fit(fr_df_fit)     

    # extract labels and calculate silhoutte score
    labels = kmeans.labels_
    print (ic, skmet.silhouette_score(fr_df_fit, labels))


######display clsuters
nc = 3
kmeans = cluster.KMeans(n_clusters=nc)
kmeans.fit(fr_df_fit)     

# extract labels and cluster centres
labels = kmeans.labels_
cen = kmeans.cluster_centers_

plt.figure(figsize=(6.0, 6.0), dpi=600)
# scatter plot with colours selected using the cluster numbers
plt.scatter(fr_df_fit["Population growth (annual %)"], fr_df_fit["Cereal yield (kg per hectare)"], c=labels, cmap="tab10")
# colour map Accent selected to increase contrast between colours

# show cluster centres
xc = cen[:,0]
yc = cen[:,1]
plt.scatter(xc, yc, c="k", marker="d", s=80)
# c = colour, s = size

plt.xlabel("Population growth (annual %)")
plt.ylabel("Cereal yield (kg per hectare)")
plt.title("3 clusters")
plt.show()
