import csv
import itertools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv(r'C:\Users\kostikas\Downloads\ComputationalAssignment2022\housing.csv')
sf= pd.DataFrame(data,columns=['longitude','latitude','ocean_proximity'])
vectored_sea = pd.get_dummies(sf.ocean_proximity)
#vectored_long = pd.get_dummies(sf.longitude)
#vectored_latit = pd.get_dummies(sf.latitude)
#print(vectored_long)
#print(vectored_latit)
print(vectored_sea)
#vectored_latit.to_csv("hot_vector_latitude.csv",index=False)
#vectored_long.to_csv("hot_vector_longitude.csv",index=False)
vectored_sea.to_csv("vectored_sea.csv",index=False)