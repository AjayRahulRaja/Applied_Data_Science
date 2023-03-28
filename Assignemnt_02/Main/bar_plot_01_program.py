#importing module and library
import driverProgram as dp
import matplotlib.pyplot as plt
import pandas as pd

#Calling all the selected countries' data and assigning them again it here
France = dp.France
United_Kingdom = dp.United_Kingdom
Japan = dp.Japan
Cuba = dp.Cuba
Iraq = dp.Iraq
Colombia = dp.Colombia
Australia = dp.Australia
Algeria = dp.Algeria
India = dp.India
#Extracting each countries' Population growth rate over few decades
France_1960 = France.loc['1960']
France_1970 = France.loc['1970']
France_1980 = France.loc['1980']
France_1990 = France.loc['1990']
France_2000 = France.loc['2000']
France_2010 = France.loc['2010']
France_2020 = France.loc['2020']
France_bar_urban_population_list=["France",France_1960['Population growth (annual %)'], \
                                  France_1970['Population growth (annual %)'], \
                                  France_1980['Population growth (annual %)'], \
                                  France_1990['Population growth (annual %)'], \
                                  France_2000['Population growth (annual %)'], \
                                  France_2010['Population growth (annual %)'], \
                                  France_2020['Population growth (annual %)']]
#Collecting United Kingdom's Data
uk_1960 = United_Kingdom.loc['1960']
uk_1970 = United_Kingdom.loc['1970']
uk_1980 = United_Kingdom.loc['1980']
uk_1990 = United_Kingdom.loc['1990']
uk_2000 = United_Kingdom.loc['2000']
uk_2010 = United_Kingdom.loc['2010']
uk_2020 = United_Kingdom.loc['2020']
uk_bar_urban_population_list=["United Kingdom",uk_1960['Population growth (annual %)'], \
                              uk_1970['Population growth (annual %)'], \
                              uk_1980['Population growth (annual %)'], \
                              uk_1990['Population growth (annual %)'], \
                              uk_2000['Population growth (annual %)'], \
                              uk_2010['Population growth (annual %)'], \
                              uk_2020['Population growth (annual %)']]
#Collecting India's Data
india_1960 = India.loc['1960']
india_1970 = India.loc['1970']
india_1980 = India.loc['1980']
india_1990 = India.loc['1990']
india_2000 = India.loc['2000']
india_2010 = India.loc['2010']
india_2020 = India.loc['2020']
india_bar_urban_population_list=["India",india_1960['Population growth (annual %)'], \
                                 india_1970['Population growth (annual %)'], \
                                 india_1980['Population growth (annual %)'], \
                                 india_1990['Population growth (annual %)'], \
                                 india_2000['Population growth (annual %)'], \
                                 india_2010['Population growth (annual %)'], \
                                 india_2020['Population growth (annual %)']]
#Collecting Japan's Data
japan_1960 = Japan.loc['1960']
japan_1970 = Japan.loc['1970']
japan_1980 = Japan.loc['1980']
japan_1990 = Japan.loc['1990']
japan_2000 = Japan.loc['2000']
japan_2010 = Japan.loc['2010']
japan_2020 = Japan.loc['2020']
japan_bar_urban_population_list=["Japan",japan_1960['Population growth (annual %)'], \
                                 japan_1970['Population growth (annual %)'], \
                                 japan_1980['Population growth (annual %)'], \
                                 japan_1990['Population growth (annual %)'], \
                                 japan_2000['Population growth (annual %)'], \
                                 japan_2010['Population growth (annual %)'], \
                                 japan_2020['Population growth (annual %)']]
#Collecting Cuba's Data
cuba_1960 = Cuba.loc['1960']
cuba_1970 = Cuba.loc['1970']
cuba_1980 = Cuba.loc['1980']
cuba_1990 = Cuba.loc['1990']
cuba_2000 = Cuba.loc['2000']
cuba_2010 = Cuba.loc['2010']
cuba_2020 = Cuba.loc['2020']
cuba_bar_urban_population_list=["Cuba",cuba_1960['Population growth (annual %)'], \
                                cuba_1970['Population growth (annual %)'], \
                                cuba_1980['Population growth (annual %)'], \
                                cuba_1990['Population growth (annual %)'], \
                                cuba_2000['Population growth (annual %)'], \
                                cuba_2010['Population growth (annual %)'], \
                                cuba_2020['Population growth (annual %)']]
#Collecting Colombia's Data
colombia_1960 = Colombia.loc['1960']
colombia_1970 = Colombia.loc['1970']
colombia_1980 = Colombia.loc['1980']
colombia_1990 = Colombia.loc['1990']
colombia_2000 = Colombia.loc['2000']
colombia_2010 = Colombia.loc['2010']
colombia_2020 = Colombia.loc['2020']
colombia_bar_urban_population_list=["Colombia",colombia_1960['Population growth (annual %)'], \
                                    colombia_1970['Population growth (annual %)'], \
                                    colombia_1980['Population growth (annual %)'], \
                                    colombia_1990['Population growth (annual %)'], \
                                    colombia_2000['Population growth (annual %)'], \
                                    colombia_2010['Population growth (annual %)'], \
                                    colombia_2020['Population growth (annual %)']]
#Collecting Iraq's Data
iraq_1960 = Iraq.loc['1960']
iraq_1970 = Iraq.loc['1970']
iraq_1980 = Iraq.loc['1980']
iraq_1990 = Iraq.loc['1990']
iraq_2000 = Iraq.loc['2000']
iraq_2010 = Iraq.loc['2010']
iraq_2020 = Iraq.loc['2020']
iraq_bar_urban_population_list=["Iraq", iraq_1960['Population growth (annual %)'], \
                                iraq_1970['Population growth (annual %)'], \
                                iraq_1980['Population growth (annual %)'], \
                                iraq_1990['Population growth (annual %)'], \
                                iraq_2000['Population growth (annual %)'], \
                                iraq_2010['Population growth (annual %)'], \
                                iraq_2020['Population growth (annual %)']]
#Collecting Algeria's Data
algeria_1960 = Algeria.loc['1960']
algeria_1970 = Algeria.loc['1970']
algeria_1980 = Algeria.loc['1980']
algeria_1990 = Algeria.loc['1990']
algeria_2000 = Algeria.loc['2000']
algeria_2010 = Algeria.loc['2010']
algeria_2020 = Algeria.loc['2020']
algeria_bar_urban_population_list=["Algeria",algeria_1960['Population growth (annual %)'], \
                                   algeria_1970['Population growth (annual %)'], \
                                   algeria_1980['Population growth (annual %)'], \
                                   algeria_1990['Population growth (annual %)'], \
                                   algeria_2000['Population growth (annual %)'], \
                                   algeria_2010['Population growth (annual %)'], \
                                   algeria_2020['Population growth (annual %)']]
#Collecting Australia's Data
australia_1960 = Australia.loc['1960']
australia_1970 = Australia.loc['1970']
australia_1980 = Australia.loc['1980']
australia_1990 = Australia.loc['1990']
australia_2000 = Australia.loc['2000']
australia_2010 = Australia.loc['2010']
australia_2020 = Australia.loc['2020']
australia_bar_urban_population_list=["Australia", australia_1960['Population growth (annual %)'], \
                                     australia_1970['Population growth (annual %)'], \
                                     australia_1980['Population growth (annual %)'], \
                                     australia_1990['Population growth (annual %)'], \
                                     australia_2000['Population growth (annual %)'], \
                                     australia_2010['Population growth (annual %)'], \
                                     australia_2020['Population growth (annual %)']]
#Saving all the essential parameters to plot a bar graph
bar_plot = pd.DataFrame([
    France_bar_urban_population_list,
    uk_bar_urban_population_list,
    india_bar_urban_population_list,
    japan_bar_urban_population_list,
    cuba_bar_urban_population_list,
    colombia_bar_urban_population_list,
    iraq_bar_urban_population_list,
    algeria_bar_urban_population_list,
    australia_bar_urban_population_list],
    columns=["Country_Name", "1960", "1970", "1980", "1990", "2000", "2010", "2020"])
#plotting bar graph
bar_plot.plot(x='Country_Name',
              kind='bar',
              stacked=False,
              title='Population Growth Over Years', figsize=(10,5))
plt.xticks(rotation=45)
plt.xlabel("Country")
plt.ylabel("population in percentage")
plt.ylim(0, 4, 0.5)
plt.legend(loc='upper left')
plt.savefig('C:/Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj 02/plots/New folder/bar_01.png',
            dpi=400,
            bbox_inches ="tight",
            pad_inches = 1,
            transparent = False,
            orientation ='landscape')
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()