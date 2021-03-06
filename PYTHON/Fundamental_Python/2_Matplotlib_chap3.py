#1. IF, ELIF, ELSE
z = 7
if z % 2 == 0 : # True
    print('z is divisible by 2')
elif z % 3 == 0 :
    print('z is divisible by 3')
else :
    print('unknown')

#%%
# two variables as:
room = 'bed'
area = 14.0
# if room = kit --> looking around in the kitchen 
# elif == bed --> looking around in the bedroom
# looking around elsewhere

# if area > 15 --> big place! 
# elif > 10 --> medium size, nice!
# else pretty small
if room == 'kit' :
    print('looking around in the kitchen')
elif room == 'bet' :
    print('looking around in the bedroom')
else :
    print('looking around elsewhere')
if area > 15 :
    print('big place!')
elif area > 10 :
    print('medium size, nice!')
else :
    print('pretty small')
# %%

#2. Filtering pandas DataFrames
# import bric.csv
import pandas as pd
brics = pd.read_csv('brics.csv', sep = ',')
brics_1 = brics[['country']]
brics_list = brics_1.values.tolist()
print(brics_list[0])

# %%
# find all observations in cars where drives_right is True
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)
dr = cars['drives_right'] == False
print(cars[dr])
# %%
#set all lines to 1 line
sel = cars[cars['drives_right']]
print(sel)
# %%
# which countries have a high cars per capita > 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]
print(car_maniac)

# %%
# countries have cars > 10 and < 80 - use np.logical_and() _or() _not()
import numpy as np
medium_car = cars[np.logical_and(cars['cars_per_cap']>10, cars['cars_per_cap']<80)]
print(medium_car)
# %%
