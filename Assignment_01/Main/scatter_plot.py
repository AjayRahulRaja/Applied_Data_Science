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

#Storing IMDB score column of US data
us_data_1950_to_1990_imdb_score = us_data_1950_to_1990['imdb_score']
us_data_1990_to_2020_imdb_score = us_data_1990_to_2020['imdb_score']

#Plot: Scatter Plot
plt.style.use('ggplot')
plt.figure(figsize=(8, 10))

plt.subplot(2, 1, 1)
plt.scatter(us_data_1950_to_1990_imdb_score.value_counts().index, us_data_1950_to_1990_imdb_score.value_counts(), linewidths=2, color="green", label="United States")
plt.title("IMDB score for films produced between 1950 and 1990 in the United States", size=14, y=0.991)
plt.xlabel("IMDB score")
plt.ylabel("Number of films")
plt.legend()

plt.subplot(2, 1, 2)
plt.scatter(us_data_1990_to_2020_imdb_score.value_counts().index, us_data_1990_to_2020_imdb_score.value_counts(), linewidths=2, marker ="^", color="green", label="United States")
plt.title("IMDB score for films produced between 1990 and 2020 in the United States", size=14, y=0.991)
plt.xlabel("IMDB score")
plt.ylabel("Number of films")
plt.legend()
plt.show()