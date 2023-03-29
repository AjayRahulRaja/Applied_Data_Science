"""
Module to create a heat plot

@author: ajay rahul
"""

#importing module and library
import driverProgram as dp
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
import stats
import seaborn as sns

#Calling France's data from the driverProgram
France = dp.France
#Filtering and saving France's different years and different parameter.
France_heat_map_parameters = France.loc[
     ('1960', '1970', '1980', '1990', '2000', '2010', '2020'),
     ('Population growth (annual %)',
      'Agricultural land (% of land area)',
      'Arable land (% of land area)',
      'Forest area (% of land area)',
      'Cereal yield (kg per hectare)',
      'CO2 emissions (kg per PPP $ of GDP)',
      'CO2 emissions (kt)',
      'CO2 emissions from gaseous fuel consumption (% of total)',
      'CO2 emissions from solid fuel consumption (% of total)',
      'CO2 emissions from liquid fuel consumption (% of total)')]
#calculating correlation for France
corr_france_heat_map = France_heat_map_parameters.corr()
#getting France flag color for heat map custom color
def get_custom_color_palette():
     return LinearSegmentedColormap.from_list("", [
          dp.create_color(0,85,164), 
          dp.create_color(255,255,255), 
          dp.create_color(239,65,53)
     ])
cmap = get_custom_color_palette()
#plotting heat map
plt.figure(figsize=(8, 6))
sns.heatmap(corr_france_heat_map, cmap=cmap, annot=True, linewidths=0.5, annot_kws={'size': 10})
plt.title('France')
plt.savefig('C:/Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj 02/plots/New folder/fra_heat_map_dpi.png',
            dpi=400,
            bbox_inches ="tight",
            pad_inches = 1,
            transparent = False,
            orientation ='landscape')
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()