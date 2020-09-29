#%%
# print out as column use for loop
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for x in areas:
    print(x)

# %%
# print out with string index by enumerate():
for i, a in enumerate(areas):
    print('room ' + str(i) + ': ' + str(a))
# %%
# print out with string index started at 1 by enumerate():
for i, a in enumerate(areas):
    print('room ' + str(i + 1) + ': ' + str(a))
# %%
# print out list of lists with for loop
house =[['hallway',11.25],
        ['kitchen', 18.0],
        ['living room', 20.0],
        ['bedroom', 10.75],
        ['bathroom', 9.50]]
for x, y in house:
    print('the ' + x + ' is ' + str(y) + ' sqm')
# %%
# Loop over dictionary
europe = { 'spain':'madrid', 'france': 'paris', 'germany':'berlin', 'norway':'oslo' }
for key, value in europe.items():
    print('the capital of ' + key + ' is ' + str(value))
# %%
# loop for 1D Numpy array
import csv
file = open('baseball_height_in.csv')
reader = csv.reader(file)
data = list(reader)
height = []
for x in data:
    for string in x:
        height.append(int(string))

import numpy as np
np_height = np.array(height)
for x in np_height:
    print(str(x) + ' inches')
# %%
# Loop for 2D Numpy array
import ast
file1 = open('baseball_heightin_weightpound.csv')
baseball = file1.read().splitlines()
baseball = ast.literal_eval(''.join(baseball))
print(baseball)
np_baseball = np.array(baseball)
for x in np.nditer(np_baseball):
    print(x)
# %%
# Loop over DataFrame
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

for lab, row in cars.iterrows():
    print(lab)
    print(row)

# %%
# adapt for loop

import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

for lab, row in cars.iterrows():
    print(lab + ': ' + str(row['cars_per_cap']))
# %%
# add column in DataFrame
for lab, row in cars.iterrows():
    cars.loc[lab,'COUNTRY'] = row['country'].upper()

print(cars)
# %%
# add column without For loop by using apply()
cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)
# %%
