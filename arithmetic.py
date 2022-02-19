import csv
import itertools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mlxtend.preprocessing import minmax_scaling

#importing data
data = pd.read_csv(r'C:\Users\kostikas\Downloads\ComputationalAssignment2022\housing.csv')
sf= pd.DataFrame(data,columns=['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value'])
sf_longitude = sf.longitude
sf_latitude = sf.latitude
sf_house_age = sf.housing_median_age
sf_rooms = sf.total_rooms
sf_debrooms = sf.total_bedrooms
sf_population = sf.population
sf_households= sf.households
sf_income = sf.median_income
sf_house_value = sf.median_house_value
#fill nan of bedroom
idk = int(sf_debrooms.mean())
sf_debrooms= sf_debrooms.fillna(idk)
#scale
lat_scaled = minmax_scaling(sf_latitude,columns=[0],min_val=0,max_val=1).tolist()
long_scaled = minmax_scaling(sf_longitude,columns=[0],min_val=0,max_val=1).tolist()
house_scaled = minmax_scaling(sf_house_age,columns=[0],min_val=0,max_val=1).tolist()
rooms_scaled = minmax_scaling(sf_rooms,columns=[0],min_val=0,max_val=1).tolist()
bedroom_scaled = minmax_scaling(sf_debrooms,columns=[0],min_val=0,max_val=1).tolist()
population_scaled = minmax_scaling(sf_population,columns=[0],min_val=0,max_val=1).tolist()
household_scaled = minmax_scaling(sf_households,columns=[0],min_val=0,max_val=1).tolist()
income_scaled = minmax_scaling(sf_income,columns=[0],min_val=0,max_val=1).tolist()
value_scaled = minmax_scaling(sf_house_value,columns=[0],min_val=0,max_val=1).tolist()
#iterate to list
long_scaled = list(itertools.chain(*long_scaled))
lat_scaled = list(itertools.chain(*lat_scaled))
house_scaled = list(itertools.chain(*house_scaled))
rooms_scaled = list(itertools.chain(*rooms_scaled))
bedroom_scaled = list(itertools.chain(*bedroom_scaled))
population_scaled = list(itertools.chain(*population_scaled))
household_scaled = list(itertools.chain(*household_scaled))
income_scaled = list(itertools.chain(*income_scaled))
value_scaled = list(itertools.chain(*value_scaled))
#make into single array
ss={"longitude": long_scaled,"latitude" : lat_scaled,"house_age" : house_scaled , "rooms_amount" : rooms_scaled,"bedrooms":bedroom_scaled,"population":population_scaled,"households":household_scaled,"income" : income_scaled,"value":value_scaled}
data = pd.DataFrame(ss)
data.to_csv("scaled.csv",index=False)