#importing module and library
import driverProgram as dp
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

#Calling France's data from the driverProgram
France = dp.France

France_heat_map_parameters = France.loc[
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
         ,'CO2 emissions from liquid fuel consumption (% of total)' )]

corr_france_heat_map = France_heat_map_parameters.corr()

def get_custom_color_palette():
     return LinearSegmentedColormap.from_list("", [
          dp.create_color(0,85,164), \
          dp.create_color(255,255,255), \
          dp.create_color(239,65,53)
     ])

cmap = get_custom_color_palette()
sns.heatmap(corr_france_heat_map, cmap=cmap, center=0)
plt.show()