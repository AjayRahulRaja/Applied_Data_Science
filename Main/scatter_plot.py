import matplotlib.pyplot as plt
import Applied_Data_Science_Viz_Proj_01 as parent_module

us_data = parent_module.us_data
fr_data = parent_module.fr_data
jp_data = parent_module.jp_data
gb_data = parent_module.gb_data
es_data = parent_module.es_data
us_data_1950_to_1990 = parent_module.us_data_1950_to_1990
us_data_1990_to_2020 = parent_module.us_data_1990_to_2020

us_data_1950_to_1990_imdb_score = us_data_1950_to_1990['imdb_score']
us_data_1990_to_2020_imdb_score = us_data_1990_to_2020['imdb_score']

#Plot: Scatter Plot
plt.style.use('ggplot')
plt.figure(figsize=(8, 10))

plt.subplot(2, 1, 1)
plt.scatter(us_data_1950_to_1990_imdb_score.value_counts().index, us_data_1950_to_1990_imdb_score.value_counts(), color="green")
plt.title("IMDB score for films produced between 1950 to 1990 in the United States", size=14, y=1.001)
plt.xlabel("IMDB score")
plt.ylabel("Number of films")

plt.subplot(2, 1, 2)
plt.scatter(us_data_1990_to_2020_imdb_score.value_counts().index, us_data_1990_to_2020_imdb_score.value_counts(), color="green")
plt.title("IMDB score for films produced between 1990 to 2020 in the United States", size=14, y=1.001)
plt.xlabel("IMDB score")
plt.ylabel("Number of films")
plt.show()