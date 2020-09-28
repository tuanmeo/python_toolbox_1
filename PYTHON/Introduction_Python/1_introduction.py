print(7+10)

savings = 100
print(savings)

growth_multiplier = 1.1
print(saving*growth_multiplier**7)
print(type(growth_multiplier))

# Create boolean and string
desc = 'compound interest'
profitable = True

# calculate with operations
year1 = savings * growth_multiplier
print(type(year1))

doubledesc = desc + desc
print(doubledesc)

result = 100 * 1.10 ** 7
print('I started with $' + str(savings) + ' and now have $' + str(result) + '. Awesome!')

pi_string = '3.1415926'
pi_float = float(pi_string)
print(type(pi_float))

# PYTHON LIST
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = [hall, kit, liv, bed, bath]
print(areas)

areas = ['hallway', hall, 'kitchen', kit,
 'living', liv, 'bedroom', bed, 'bathroom', bath]
print(areas)

house = [['hallway', hall],
        ['kitchen', kit],
        ['livingroom', liv],
        ['bedroom', bed],
        ['bathroom', bath]]
        
print(house)
print(type(house))

# print out the second, last element from areas
# print out the area of the living room
print(areas[1])
print(areas[-1])

eat_sleep_area = areas[3] + areas[-3]
print(eat_sleep_area)

downstair = areas[0:6]
upstair = areas[6:10]
print(downstair)
print(upstair)

house[-1][0] # first number for the last list, second for the first value of the list

areas[-1] = 10.50
areas[4] = 'chill zone'
print(areas)

areas_1 = areas + ['poolhouse', 24.5]
print(areas_1)

areas_2 = areas_1 + ['garage', 15.45]
print(areas_2)


#FUNCTIONS
var1 = [1,2,3,4]
var2 = True

print(type(var1))
print(len(var1))

help(complex)

first = [11.25, 18.0, 20.0]
second = [10.75,9.50]

full = first + second
print(full)

full_sorted = sorted(full, reverse=False)
print(full_sorted)

#STRING METHODS

place = 'poolhouse'
place_up = place.upper()

print(place)
print(place_up)
print(place_up.count('O'))

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas.index(20.0))
print(areas.count(9.50))

# append() -- add element
# remove() -- remove the 1st element matched 
# reverse() -- reverses the order

print(areas)
areas.append(24.5)
areas.append(15.45)
print(areas)
areas_re = areas.reverse()
print(areas)

# Define radius
r = 0.043
import math
C = 2 * math.pi * r
A = math.pi * r * r

print('Circumference: ' + str(C))
print('Area: ' + str(A))

#SELECT IMPORT  
#define of radius
r = 192500
from math import radians
dist = r * radians(12) #travel distance of Moon over 12 degrees.
print(dist)

# NUMPY
# create a list baseball
baseball = [180, 215, 210, 188, 176, 209, 200]
import numpy as np
# create numpy array
np_baseball = np.array(baseball)
print(type(np_baseball))

#Baseball players' height
import csv
import numpy as np
filepath_1 = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/baseball_height_in.csv'
file_1 = open(filepath_1)
reader_1 = csv.reader(file_1)
height_in = list(reader_1)
height_in = sum(height_in, [])
height_in = [int(i) for i in height_in]
print(height_in)
print(type(height_in))
# create numpy array from height_in:
np_height_in = np.array(height_in)
print(type(np_height_in))

# convert np_height_in to meter: * 0.0254
np_height_m = np_height_in * 0.0254
print(*np_height_m, sep = ",") #print all the entries with * and sep

#Baseball player's BMI
filepath_2 = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/baseball_weight_lb.csv'
file_2 = open(filepath_2)
reader_2 = csv.reader(file_2)
weight_lb = list(reader_2)
weight_lb = sum(weight_lb, [])
weight_lb = [int(i) for i in weight_lb]
print(weight_lb)
# create array of weight_kg: *0.453592
np_weight_kg = np.array(weight_lb) * 0.453592
# calculate the BMI
bmi = np_weight_kg/np_height_m**2

print(*bmi, sep="\n")


# Use boolean in array
# create a boolean 'numpy' array: the element of the array should be 'true'
light = np.array(bmi < 21)
print(light)
print(bmi[light])
print(type(bmi))

# Create 2D NumPy Array
import ast
filepath_3 = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/baseball_heightin_weightpound.csv'
file_3 = open(filepath_3)
baseball = file_3.read().splitlines()
baseball_1 = ast.literal_eval( ''.join(baseball))

print(baseball_1)
print(type(baseball_1))

np_baseball = np.array(baseball_1)
print(type(np_baseball))
print(np_baseball.shape)

print(np_baseball[49,:]) # 49 is the row number
# select the entire 2nd column of np_baseball: np_weight_lb
print(np_baseball[:,1])
# Print out height of 124th player
print(np_baseball[123,0])


# Update to 3 columns of baseball as height - weight - age

filepath_4 = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/baseball_height_weight_age.csv'
file_4 = open(filepath_4)
baseball = file_4.read().splitlines()
baseball = ast.literal_eval(''.join(baseball))
print(baseball)
print(type(baseball))
np_baseball = np.array(baseball)
print(np_baseball.shape)

# Update includes height - weight - age info
filepath_5 = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/baseball_height_weight_age_updated.csv'
updated = open(filepath_5)
updated = ast.literal_eval(''.join(updated))

print(type(updated))

updated = np.array(updated)
print(updated.shape)
%whos

# Print out updated data
print(np_baseball + updated)

# Create numpy array to change to meter, kilogram:
conversion = np.array([0.0254, 0.453592, 1])
print(np_baseball * conversion)

np_height_in = np_baseball[:,0]
print(np_baseball)
print(np_height_in)
print(np.mean(np_height_in))
print(np.median(np_height_in))

#Print out the sd on height
stddev = np.std(np_baseball[:, 0])
print('standard deviation: ' + str(stddev))

# Print out correlation between first and second column. 
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print('Correlation; ' + str(corr))




 import csv
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/fifa_heights_1.csv'
file = open(filepath)
reader = csv.reader(file)
data = list(reader)
heights = []
for inner_list in data:
    for string in inner_list:
        heights.append(int(string))

print(type(heights))
np_heights = np.array(heights)


import csv
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/positions copy.csv'
file = open(filepath)
data = file.read().splitlines()
print(data)
data_2 = ''.join(data)
print(data_2)
data_3 = data_2.replace("'", "").replace(" ","")
print(data_3)
positions = data_3.split(',')
print(data_4)
np_positions = np.array(positions)

gk_heights = np_heights[np_positions == 'GK']
print(gk_heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']
print(gk_heights)
# Heights of the other players: other_heights

other_heights = np_heights[np_positions != 'GK']
# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))