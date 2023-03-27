#importing module and library
import driverProgram as dp
import matplotlib.pyplot as plt

#Calling Individual countries from the main program and asssigin individually to create plot
France_plot_param = dp.France.loc[('1960', '1970', '1980', '1990', '2000', '2010'), ('Agricultural land (% of land area)', 'Forest area (% of land area)')]
United_kingdom_plot_param = dp.United_Kingdom.loc[('1960', '1970', '1980', '1990', '2000', '2010'), ('Agricultural land (% of land area)', 'Forest area (% of land area)')]
India_plot_param = dp.India.loc[('1960', '1970', '1980', '1990', '2000', '2010'), ('Agricultural land (% of land area)', 'Forest area (% of land area)')]
Japan_plot_param = dp.Japan.loc[('1960', '1970', '1980', '1990', '2000', '2010'), ('Agricultural land (% of land area)', 'Forest area (% of land area)')]
Cuba_plot_param = dp.Cuba.loc[('1960', '1970', '1980', '1990', '2000', '2010'), ('Agricultural land (% of land area)', 'Forest area (% of land area)')]
Colombia_plot_param = dp.Colombia.loc[('1960', '1970', '1980', '1990', '2000', '2010'), ('Agricultural land (% of land area)', 'Forest area (% of land area)')]
Iraq_plot_param = dp.Iraq.loc[('1960', '1970', '1980', '1990', '2000', '2010'), ('Agricultural land (% of land area)', 'Forest area (% of land area)')]
Algeria_plot_param = dp.Algeria.loc[('1960', '1970', '1980', '1990', '2000', '2010'), ('Agricultural land (% of land area)', 'Forest area (% of land area)')]
Australia_plot_param = dp.Australia.loc[('1960', '1970', '1980', '1990', '2000', '2010'), ('Agricultural land (% of land area)', 'Forest area (% of land area)')]

#plotting line plot
plt.figure(figsize=(8, 6))
plt.plot(France_plot_param.index, France_plot_param['Agricultural land (% of land area)'], label='France', ls='--')
plt.plot(United_kingdom_plot_param.index, United_kingdom_plot_param['Agricultural land (% of land area)'], label='United Kingdom', ls='--')
plt.plot(India_plot_param.index, India_plot_param['Agricultural land (% of land area)'], label='India', ls='--')
plt.plot(Japan_plot_param.index, Japan_plot_param['Agricultural land (% of land area)'], label='Japan', ls='--')
plt.plot(Cuba_plot_param.index, Cuba_plot_param['Agricultural land (% of land area)'], label='Cuba', ls='--')
plt.plot(Colombia_plot_param.index, Colombia_plot_param['Agricultural land (% of land area)'], label='Colombia', ls='--')
plt.plot(Iraq_plot_param.index, Iraq_plot_param['Agricultural land (% of land area)'], label='Iraq', ls='--')
plt.plot(Algeria_plot_param.index, Algeria_plot_param['Agricultural land (% of land area)'], label='Algeria', ls='--')
plt.plot(Australia_plot_param.index, Australia_plot_param['Agricultural land (% of land area)'], label='Australia', ls='--')

plt.xlabel('Years')
plt.ylabel('% of land area')
plt.title('Agricultural Land (% of land area) over decades')
plt.xlim(0, 5)
plt.ylim(0, 85, 10)
plt.legend(bbox_to_anchor= (1.015, 1.015))
plt.show()

