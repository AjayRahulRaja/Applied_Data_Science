#importing module and library
import driverProgram as dp
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

#Calling Japan's data from the driverProgram
Japan = dp.Japan
#Filtering and saving Japan's different years and different parameter.
Japan_heat_map_parameters = Japan.loc[
    ('1960', '1970', '1980', '1990', '2000', '2010', '2020'), \
    ('Population growth (annual %)' \
         ,'Agricultural land (% of land area)' \
         ,'Arable land (% of land area)' \
         ,'Forest area (% of land area)' \
         ,'Cereal yield (kg per hectare)' \
         ,'CO2 emissions (kg per PPP $ of GDP)' \
         ,'CO2 emissions (kt)' \
         ,'CO2 emissions from gaseous fuel consumption (% of total)' \
         ,'CO2 emissions from solid fuel consumption (% of total)' \
         ,'CO2 emissions from liquid fuel consumption (% of total)'
     )]
#calculating Japan's correlation
corr_Japan_heat_map = Japan_heat_map_parameters.corr()
#getting Japan's flag color for heat map custom color
def get_custom_color_palette():
    return LinearSegmentedColormap.from_list("", [
        dp.create_color(255, 255, 255),
        dp.create_color (188, 0, 45)
    ])
cmap = get_custom_color_palette()
#plotting heat map
plt.figure(figsize=(12, 8))
sns.heatmap(corr_Japan_heat_map, cmap=cmap, center=0, annot=True, linewidths=0.5, annot_kws={'size': 10})
plt.title("Japan")
plt.savefig('C:/Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj 02/plots/New folder/jpn_heat_map_dpi.png',
            dpi=400,
            bbox_inches ="tight",
            pad_inches = 1,
            transparent = False,
            orientation ='landscape')
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()