#FIFA FILE

#heights = 

np_heights = np.array(heights)
np_positions = np.array(positions)


import csv
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/fifa_heights_1.csv'
file = open(filepath)
reader = csv.reader(file)
data = list(reader)
print(data)
data = sum(data, [])
print(data)


 import csv
 import numpy as np
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/fifa_heights_1.csv'
file = open(filepath)
reader = csv.reader(file)
data = list(reader)
print(data)
data = sum(data, [])
print(data)
data = [int(i) for i in data]
np_data = np.array(data)
print(type(np_data))
print(np_data)


 import csv
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/fifa_heights_1.csv'
file = open(filepath)
reader = csv.reader(file)
data = list(reader)
int_list = []
for inner_list in data:
    for string in inner_list:
        int_list.append(int(string))

print(type(int_list))
print(int_list)


import csv
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/positions copy.csv'
file = open(filepath)
data = file.read().splitlines()
print(data)
data_2 = ''.join(data)
print(data_2)
data_3 = data_2.replace("'", "").replace(" ","")
print(data_3)
positions = data_3.split(',')
print(positions)

import csv
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/positions copy.csv'
with open(filepath,'rt') as f:
    print(next(csv.reader(f,delimiter = ',', quotechar = "'", skipinitialspace = True)))

filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/positions copy.csv'
with open (filepath,'r') as f:
    data = f.read()
data = [s.replace("'","") for s in data.split(',')]
print(type(data))
print(data)



