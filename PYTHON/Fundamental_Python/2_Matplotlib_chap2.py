# USE INDEX OF TWO LIST
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]

ind_alb = countries.index("albania")
pop[ind_alb]
# not convenient

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', 'france': 'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe
print(europe)
# print out keys of europe
print(europe.keys())
# print out value that belongs to key 'norway'
print(europe['norway'])

# add italy to europe
europe['italy'] = 'rome'
europe['poland'] = 'warsaw'

print(europe['italy'])
print(europe)

# delete key 'italy'
del(europe['italy'])
print(europe)

# dictionary can contain anything, even other lists
europe1 = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# print out the capital of France
print(europe1['france']['capital'])
# create data as capital rome, pop 59.83
data = {'capital':'rome', 'population':59.83}
# add data to europe1 as italy
europe1['italy'] = data
print(europe1)




# DICTIONARY TO DATAFRAME
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

import pandas as pd
# create dictionary my_dict with lists above
my_dict = {
    'country':names,
    'drives_right':dr,
    'cars_per_cap':cpc
}
#build DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict, index = False)
print(cars)
#Define row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels
print(cars)

#import cars.csv by pandas
cars = pd.read_csv('/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Fundamental_Python/cars.csv', index_col=0)
print(cars)


# WORK WITH DATAFRAME
#print country as pandas series
print(cars['country'])
# print country as pandas dataframe
print(cars[['country']])
# print country and drives_right 
print(cars[['country', 'drives_right']])
# print out first 3 observations of cars
print(cars[0:3])
# print out 4th, 5th, and 5th observation
print(cars[3:6])

#print out observation of Japan use loc as series
print(cars.loc['JAP'])
# print out observation of Australia and Egypt as dataframe
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1,6]])

# we can extract records 
# print out drives_right values of Morocco
print(cars.loc[['MOR'],['drives_right']])
print(cars.iloc[[5],[2]])
# print sub-DataFrame as RU, MOR - country, drive_right
print(cars.loc[['RU', 'MOR'],['country','drives_right']])
# print out drives_right as series
print(cars.loc[:,['drives_right']])
print(cars.loc[:,'drives_right']) # as series data
# print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])