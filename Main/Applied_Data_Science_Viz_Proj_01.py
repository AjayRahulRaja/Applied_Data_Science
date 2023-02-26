import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj/HBO_dataset_kaggle/titles.csv")

#Read the data for five different countries
us_data = df[df['production_countries']=="['US']"]
fr_data = df[df['production_countries']=="['FR']"]
jp_data = df[df['production_countries']=="['JP']"]
gb_data = df[df['production_countries']=="['GB']"]
es_data = df[df['production_countries']=="['ES']"]

x=df['production_countries'].value_counts()
x

pd.set_option('display.max_row', None)

#making a list for 5 countries
country_list = [us_data, fr_data, jp_data, gb_data, es_data]
country_names_list = ["United States", "France", "Japan", "Great Britain", "Spain"]

def numberOfMoviesPerCountries(country_list):
    result = []
    for x in country_list:
        result_value = x['production_countries'].value_counts()
        result_value_without_index = result_value.to_string(index=False)
        result.append(result_value_without_index)
    return result

numberOfMoviesPerCountries(country_list)

number_of_movies_per_countries = numberOfMoviesPerCountries(country_list)
number_of_movies_pers_countries_int = [int(int_to_str_conversion) for int_to_str_conversion in number_of_movies_per_countries]
for x in number_of_movies_pers_countries_int:
    print(type(x))
total = sum(number_of_movies_pers_countries_int)

plt.style.use('ggplot')
plt.figure(figsize=(7, 7))
plt.pie(number_of_movies_per_countries, autopct=lambda p: '{:.0f}'.format(p * total / 100), labels=country_names_list, shadow=True, startangle=90)
plt.title("Number of HBO films produced in five countries from 1901 to 2020")
plt.legend(bbox_to_anchor=(1.25, 0.95))
plt.show()


#Analysing United States Data
us_data_1990_to_2020 = us_data[(us_data['release_year'] > 1990) & (us_data['release_year'] < 2020)]
us_data_1950_to_1990 = us_data[(us_data['release_year'] > 1950) & (us_data['release_year'] < 1990)]

plt.style.use('ggplot')
plt.figure(figsize=(10, 10))

plt.subplot(2, 1, 1)
plt.bar(us_data_1950_to_1990['release_year'].value_counts().index, us_data_1950_to_1990['release_year'].value_counts(), color='blue')
plt.xlim(1950, 1990)
plt.ylim(0, 25)
plt.title("Films produced between 1950 and 1990 in United States")

plt.subplot(2, 1, 2)
plt.bar(us_data_1990_to_2020['release_year'].value_counts().index, us_data_1990_to_2020['release_year'].value_counts(), color='blue')
plt.title("Films produced between 1990 and 2020 in United States")

plt.show()

us_data_1950_to_1990 = us_data[(us_data['release_year'] > 1950) & (us_data['release_year'] < 1990)]

us_data_1990_to_2020_imdb_score = us_data_1990_to_2020['imdb_score']
us_data_1950_to_1990_imdb_score = us_data_1950_to_1990['imdb_score']

plt.style.use('ggplot')
plt.figure(figsize=(8, 10))

plt.subplot(2, 1, 1)
plt.scatter(us_data_1950_to_1990_imdb_score.value_counts().index, us_data_1950_to_1990_imdb_score.value_counts(), color="green")
plt.title("IMDB score for films produces in United States from 1950 to 1990")

plt.subplot(2, 1, 2)
plt.scatter(us_data_1990_to_2020_imdb_score.value_counts().index, us_data_1990_to_2020_imdb_score.value_counts(), color="green")
plt.title("IMDB score for films produces in United States from 1990 to 2000")

plt.show()

# df['age_certification'].value_counts()

# us_data_1970_to_2000_age_certi = us_data_1970_to_2000['age_certification'].value_counts()
# fra_data_1970_to_2000_age_certi = fra_data_1970_to_2000['age_certification'].value_counts()
# jp_data_1970_to_2000_age_certi = jp_data_1970_to_2000['age_certification'].value_counts()
# gb_data_1970_to_2000_age_certi = gb_data_1970_to_2000['age_certification'].value_counts()
# es_data_1970_to_2000_age_certi = es_data_1970_to_2000['age_certification'].value_counts()

# plt.plot(us_data_1970_to_2000_age_certi, color=' ')
# plt.show()

# df.head(1)

# x=us_data_1970_to_2000['runtime'].value_counts()
# plt.bar(x.index, x)
# plt.show()
# df['age_certification'].value_counts()