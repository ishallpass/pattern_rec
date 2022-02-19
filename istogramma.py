import statistics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
#histogram frequency with density and probability
def freq_histogram(data,name_of_x,name_of_y,figure,title,bin2) :
    plt.figure(figure)
    #density allows us to visuallize wiiith probability density
    plt.hist(data,bins=bin2,density=True,color="red")
    plt.title(title)
    plt.xlabel(name_of_x)
    plt.ylabel(name_of_y)
    return plt

#reading the data frames
data = pd.read_csv(r'C:\Users\kostikas\Downloads\ComputationalAssignment2022\housing.csv')
sf= pd.DataFrame(data,columns=['longitude','latitude','ocean_proximity','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value'])

sf_house_age = sf.housing_median_age
sf_rooms = sf.total_rooms
sf_debrooms = sf.total_bedrooms
sf_population = sf.population
sf_households= sf.households
sf_income = sf.median_income
sf_sea = sf.ocean_proximity
sf_longitude = sf.longitude
sf_latitude = sf.latitude
sf_house = sf.median_house_value


house_age = freq_histogram(sf_house_age,"Median age of house","frequency",10,"Den prob for house age",10)
room_total = freq_histogram(sf_rooms,"Median amount of rooms","frequency",2,"Den prob for total rooms",10)
bedrooms_total = freq_histogram(sf_debrooms,"Median amount of bedrooms","frequency",3,"Den prob for bedrooms",10)
population_total = freq_histogram(sf_population,"Median amount of people","frequency",4,"Den prob for population",10)
household_total = freq_histogram(sf_households,"Median amount of households","frequency",5,"Den prob for households",10)
total_income = freq_histogram(sf_income,"Median amount of income","frequency",6,"Den prob for income",14)
#total_sea_range = freq_histogram(sf_sea,"Ocean proximity from properties","frequency",7,"Den prob for ocean proximity",4)
total_longitude = freq_histogram(sf_longitude,"logitude of research","freq",8,"Den prob for longitude",20)
total_latitude = freq_histogram(sf_latitude,"Latitude of research","frequency",9,"Den prob for latitude",20)
plt.show()