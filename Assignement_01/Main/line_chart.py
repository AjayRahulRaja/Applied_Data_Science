import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Applied_Data_Science_Viz_Proj_01 as parent_module

#Reading variables from Applied_Data_Science_Viz_Proj_01 python file
#Reading five countries' data
us_data = parent_module.us_data
fr_data = parent_module.fr_data
jp_data = parent_module.jp_data
gb_data = parent_module.gb_data
es_data = parent_module.es_data

#Reading United States' data between 1950 and 1990
us_data_1950_to_1990 = parent_module.us_data_1950_to_1990
us_data_1990_to_2020 = parent_module.us_data_1990_to_2020

#Analysing data for four countries between 2000 and 2020
gb_data_2000_to_2020 = parent_module.gb_data_2000_to_2020
fr_data_2000_to_2020 = parent_module.fr_data_2000_to_2020
jp_data_2000_to_2020 = parent_module.jp_data_2000_to_2020
es_data_2000_to_2020 = parent_module.es_data_2000_to_2020

def filmsBetween2000To2020(country_list_2000_to_2020):
    """
    This method takes four countries' entries and return the release_year of each countries' count
    :param country_list_2000_to_2020: List of four different countries as DataFrame datatype
    :return: 2D list of each countries' release year and it's count
    """
    result = []
    for x in country_list_2000_to_2020:
        result_value = x['release_year'].value_counts()
        result_value_sorted = result_value.sort_index()
        result_value_to_list = [result_value_sorted]
        result.append(result_value_to_list)
    return result

country_list_2000_to_2020 = [gb_data_2000_to_2020, fr_data_2000_to_2020, jp_data_2000_to_2020, es_data_2000_to_2020]
films_between_2000_to_2020 = filmsBetween2000To2020(country_list_2000_to_2020)

gb_2000_to_2020 = pd.DataFrame(films_between_2000_to_2020[0]).T
fr_2000_to_2020 = pd.DataFrame(films_between_2000_to_2020[1]).T
jp_2000_to_2020 = pd.DataFrame(films_between_2000_to_2020[2]).T
es_2000_to_2020 = pd.DataFrame(films_between_2000_to_2020[3]).T


#Plot: Line Plot
plt.figure(figsize=(16, 6))

plt.plot(gb_2000_to_2020, label="Great Britain")
plt.plot(fr_2000_to_2020, label="France", linestyle="dotted")
plt.plot(jp_2000_to_2020, label="Japan", linestyle="dotted")
plt.plot(es_2000_to_2020, label="Spain", ls="--")

plt.title("Number of films produced by four countries between 2000 and 2020")
plt.xlabel("Year")
plt.ylabel("Number of films")
plt.xticks(np.arange(2000, 2021, 2))
plt.yticks(np.arange(0, 15, 2))
plt.legend(loc="upper left")
plt.show()