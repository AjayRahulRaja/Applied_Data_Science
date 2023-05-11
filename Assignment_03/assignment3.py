# -*- coding: utf-8 -*-
"""
Created on Mon May 01 15:14:25 2023

@author: ajay rahul
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cluster_tools as ct
import sklearn.cluster as cluster
import sklearn.metrics as skmet
import scipy.optimize as opt
import errors as err


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


def linfunc(x, a, b):
    """ Function for fitting
    x: independent variable
    a, b: parameters to be fitted
    """
    y = a*x + b
    return y


# main code
df = pd.read_excel("API_19_DS2_en_excel_v2_4903056.xls", header=3)
#Discovering data using .describe()
df.describe()
#Redundant Columns to be removed
removeColumns=['Country Code', 'Indicator Code']


new_df = transformDf(df, removeColumns)

year = 2014

# fields to be filtered
fields = ['Population, total',
      'Agricultural land (sq. km)',
      'Arable land (% of land area)',
      'Forest area (sq. km)',
      'Cereal yield (kg per hectare)',
      'Electricity production from oil sources (% of total)',
      'CO2 emissions (kt)',
      'CO2 emissions from gaseous fuel consumption (kt)',
      'CO2 emissions from solid fuel consumption (kt)',
      'CO2 emissions from liquid fuel consumption (kt)']

# filter the dataframe with fields and year
mod_df = filterFieldsAndYear(new_df, fields, year)

hm_df = transformDf2(mod_df)

hm_df.to_csv('hm.csv')
# type cast all fields except Country to float64
for i in fields:
    if i != 'Country':
        hm_df[i] = hm_df[i].astype('float64')


# heat map for the world data
plt.figure()
ct.map_corr(hm_df)
plt.title('Heatmap')
plt.show()

# scatter matrix
plt.figure(dpi=600)
axes = pd.plotting.scatter_matrix(hm_df)
for ax in axes.flatten():
    ax.xaxis.label.set_rotation(90)
    ax.yaxis.label.set_rotation(0)
    ax.yaxis.label.set_ha('right')
plt.tight_layout()    # helps to avoid overlap of labels
plt.show()

###########finding n clusters
# extract columns for fitting. 
df_fit = hm_df[['CO2 emissions (kt)',
                'Cereal yield (kg per hectare)']].copy()

# normalise dataframe and inspect result
# normalisation is done only on the extract columns. .copy() prevents
# changes in df_fit to affect df_fish. This make the plots with the 
# original measurements
df_fit, df_min, df_max = ct.scaler(df_fit)
print(df_fit.describe())
print()

print("n   score")
# loop over trial numbers of clusters calculating the silhouette
for ic in range(2, 15):
    # set up kmeans and fit
    kmeans = cluster.KMeans(n_clusters=ic)
    kmeans.fit(df_fit)     

    # extract labels and calculate silhoutte score
    labels = kmeans.labels_
    print (ic, skmet.silhouette_score(df_fit, labels))


######display clsuters
nc = 3
kmeans = cluster.KMeans(n_clusters=nc)
kmeans.fit(df_fit)     

# extract labels and cluster centres
labels = kmeans.labels_
cen = kmeans.cluster_centers_

plt.figure(figsize=(6.0, 6.0), dpi=600)
# scatter plot with colours selected using the cluster numbers
plt.scatter(df_fit["CO2 emissions (kt)"],
            df_fit["Cereal yield (kg per hectare)"],
            c=labels, cmap="tab10")
# colour map Accent selected to increase contrast between colours

# show cluster centres
xc = cen[:,0]
yc = cen[:,1]
plt.scatter(xc, yc, c="k", marker="d", s=80)
# c = colour, s = size

plt.xlabel("CO2 emissions (kt)")
plt.ylabel("Cereal yield (kg per hectare)")
plt.title("2 clusters")
plt.show()

#fitting
# Agricultural land (sq. km)
# Forest area (sq. km)
# x = hdf['Agricultural land (sq. km)'].to_numpy()
# y = hdf['Forest area (sq. km)'].to_numpy()

popt, pcorr = opt.curve_fit(linfunc,
                            hm_df['Agricultural land (sq. km)'],
                            hm_df['Forest area (sq. km)'])
print("Fit parameters", popt)

# extract variances and calculate sigmas
sigmas = np.sqrt(np.diag(pcorr))
y1 = linfunc(hm_df['Agricultural land (sq. km)'], *popt)


plt.figure(dpi=600)
plt.title("Line Fit")
plt.plot(hm_df['Agricultural land (sq. km)'],
         hm_df['Forest area (sq. km)'], "o",
         markersize=3, label="data points")
plt.plot(hm_df['Agricultural land (sq. km)'],
         y1, label="line fit")
plt.xlabel('Agricultural land (sq. km)')
plt.ylabel('Forest area (sq. km)')
plt.legend(loc="upper left")
plt.show()
