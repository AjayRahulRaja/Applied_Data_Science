import numpy as np
import matplotlib.pyplot as plt
import Applied_Data_Science_Viz_Proj_01 as parent_module

us_data = parent_module.us_data
fr_data = parent_module.fr_data
jp_data = parent_module.jp_data
gb_data = parent_module.gb_data
es_data = parent_module.es_data
us_data_1950_to_1990 = parent_module.us_data_1950_to_1990
us_data_1990_to_2020 = parent_module.us_data_1990_to_2020

#nalysing data for four countries between 2000 and 2020
gb_data_2000_to_2020 = gb_data[(gb_data['release_year'] > 2000) & (gb_data['release_year'] < 2020)]
fr_data_2000_to_2020 = fr_data[(fr_data['release_year'] > 2000) & (fr_data['release_year'] < 2020)]
jp_data_2000_to_2020 = jp_data[(jp_data['release_year'] > 2000) & (jp_data['release_year'] < 2020)]
es_data_2000_to_2020 = es_data[(es_data['release_year'] > 2000) & (es_data['release_year'] < 2020)]

#Great Britain's Data
plot_gb_counts = gb_data_2000_to_2020['release_year'].value_counts()
plot_gb_counts=plot_gb_counts.sort_index()

#France's Data
plot_fr_counts = fr_data_2000_to_2020['release_year'].value_counts()
plot_fr_counts=plot_fr_counts.sort_index()

#Japan's Data
plot_jp_counts = jp_data_2000_to_2020['release_year'].value_counts()
plot_jp_counts=plot_jp_counts.sort_index()

#Spain's Data
plot_es_counts = es_data_2000_to_2020['release_year'].value_counts()
plot_es_counts=plot_es_counts.sort_index()

#Plot: Line Plot
plt.figure(figsize=(16, 6))

plt.plot(plot_gb_counts, label="Great Britain")
plt.plot(plot_fr_counts, label="France", linestyle="dotted")
plt.plot(plot_jp_counts, label="Japan", linestyle="dotted")
plt.plot(plot_es_counts, label="Spain", ls="--")

plt.legend(bbox_to_anchor=(1, 1))
plt.title("Number of films produced in four countries between 2000 and 2020")
plt.xlabel("Year")
plt.ylabel("Number of films")
plt.xticks(np.arange(2000, 2021, 1))
plt.yticks(np.arange(0, 15, 2))
plt.show()