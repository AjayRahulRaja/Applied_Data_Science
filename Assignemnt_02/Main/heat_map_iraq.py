#importing module and library
import driverProgram as dp
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

#Calling Iraq's data from the driverProgram
Iraq = dp.Iraq

Iraq_heat_map_parameters = Iraq.loc[
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

corr_iraq_heat_map = Iraq_heat_map_parameters.corr()

def get_custom_color_palette():
    return LinearSegmentedColormap.from_list("", [
        dp.create_color(206, 17, 38),
        dp.create_color(255, 255, 255),
        dp.create_color (0, 122, 61),
        dp.create_color(0, 0, 0)
    ])

cmap = get_custom_color_palette()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_iraq_heat_map, cmap=cmap, center=0, annot=True, linewidths=0.05)
plt.title("Iraq")
plt.show()