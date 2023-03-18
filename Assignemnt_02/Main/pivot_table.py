#importing module and library
import driverProgram as dp
import pandas as pd

#Input parametres for getPowerConsunmption function
countryList=['France', 'United Kingdom', 'India', 'Japan', 'Cuba', 'Colombia', 'Iraq', 'Algeria', 'Australia']
column='Electric power consumption (kWh per capita)'
years=['1960', '1990', '2010']

#saving the output of the function and printing it after transposing it.
x = dp.getPowerConsumption(dp.new_df1, column, years)
pivotTable=pd.DataFrame(x)
pivotTable = pivotTable.T
print(pivotTable)