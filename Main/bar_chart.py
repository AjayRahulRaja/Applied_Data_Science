import matplotlib.pyplot as plt
import Applied_Data_Science_Viz_Proj_01 as parent_module

#Analysing United States' Data
us_data = parent_module.us_data
us_data_1950_to_1990 = parent_module.us_data_1950_to_1990
us_data_1990_to_2020 = parent_module.us_data_1990_to_2020

#Plot: Bar Plot
plt.style.use('ggplot')
plt.figure(figsize=(10, 15))

plt.subplot(2, 1, 1)
plt.bar(us_data_1950_to_1990['release_year'].value_counts().index, \
        us_data_1950_to_1990['release_year'].value_counts(), color='blue')
plt.xlabel("Year")
plt.ylabel("Number of Films")
plt.xlim(1950, 1990)
plt.ylim(0, 25)
plt.title("Number of films produced between 1950 and 1990 in the United States", size=14, y=1.001)

plt.subplot(2, 1, 2)
plt.bar(us_data_1990_to_2020['release_year'].value_counts().index, \
        us_data_1990_to_2020['release_year'].value_counts(), color='blue')
plt.xlabel("Year")
plt.ylabel("Number of Films")
plt.xlim(1990, 2020)
plt.ylim(0, 120)
plt.title("Number of films produced between 1990 and 2020 in the United States", size=14, y=1.001)
plt.show()