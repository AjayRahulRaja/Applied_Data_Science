import pandas as pd
import matplotlib.pyplot as plt
import Applied_Data_Science_Viz_Proj_01 as parent_module

us_data = parent_module.us_data
fr_data = parent_module.fr_data
jp_data = parent_module.jp_data
gb_data = parent_module.gb_data
es_data = parent_module.es_data
pd.set_option('display.max_row', None)

#making a list for 5 countries
country_list = [us_data, fr_data, jp_data, gb_data, es_data]
country_names_list = ["United States", "France", "Japan", "Great Britain", "Spain"]

def numberOfMoviesPerCountries(country_list):
    """
    This method takes a list as input and calculates the count of production_countries columns for each country
    :param country_list: passing the list which holds the five countries' data
    :return: list of production_countries columns for each country in string
    """
    result = []
    for x in country_list:
        result_value = x['production_countries'].value_counts()
        result_value_without_index = result_value.to_string(index=False)
        result.append(result_value_without_index)
    return result

number_of_movies_per_countries = numberOfMoviesPerCountries(country_list)

# converting data type of production_countries from string to integer
number_of_movies_pers_countries_int = [int(int_to_str_conversion) for int_to_str_conversion in number_of_movies_per_countries]
for x in number_of_movies_pers_countries_int:
    print(type(x))
total = sum(number_of_movies_pers_countries_int)

#Plot: Pie Plot
plt.style.use('ggplot')
plt.figure(figsize=(7, 7))
plt.pie(number_of_movies_per_countries, autopct=lambda p: '{:.0f}'.format(p * total / 100), labels=country_names_list, shadow=True, startangle=90)
plt.title("Number of films available on HBO Max which are produced in five countries from 1901 to 2020", size=14, y=1.015)
plt.legend(bbox_to_anchor=(1.25, 1))
plt.show()
