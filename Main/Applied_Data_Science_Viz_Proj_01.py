import pandas as pd

#Reading the source data
df = pd.read_csv("C:/Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Applied Data Science/viz proj/HBO_dataset_kaggle/titles.csv")

#Reading data for five different countries
us_data = df[df['production_countries']=="['US']"]
fr_data = df[df['production_countries']=="['FR']"]
jp_data = df[df['production_countries']=="['JP']"]
gb_data = df[df['production_countries']=="['GB']"]
es_data = df[df['production_countries']=="['ES']"]

#Reading United States' data between 1950 and 1990
us_data_1950_to_1990 = us_data[(us_data['release_year'] > 1950) & (us_data['release_year'] < 1990)]

#Reading United States' data between 1990 and 2020
us_data_1990_to_2020 = us_data[(us_data['release_year'] > 1990) & (us_data['release_year'] < 2020)]