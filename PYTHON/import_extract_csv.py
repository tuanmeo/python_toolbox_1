import csv
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/fifa.csv'
file = open(filepath)
reader = csv.reader(file)
data = list(reader)

print(data)


x = []
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/fifa.csv'
file = open(filepath)
reader = csv.reader(file)
for i in reader:
    x.append(i[1])

print(x)
print(type(x))



filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/fifa.csv'
file = open(filepath)
reader = csv.reader(file)
next(reader)
x = []
for i in reader:
    x.append([i[1], float(i[2])])

for item in x:
    print(item)

    print(type(item))


filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/fifa.csv'
file = open(filepath)
reader = csv.reader(file)
next(reader)
x = []
for i in reader:
    x.append([i[1], float(i[2])])

for item in x:
    #print(item)
    import numpy as np
    new_array = np.array(item)
    print(new_array)



#Final appropriate solution
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/fifa.csv'
file = open(filepath)
reader = csv.reader(file)
next(reader)
x = []
for i in reader:
    x.append([i[1], float(i[2])])

data_1 = x[:]
print(data_1)
import numpy as np
data_2 = np.array(data_1)
print(data_2.shape)



#Option 2
import csv
with open('/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/fifa.csv', 'rU') as infile:
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]

names = data['name']
print(names)

#don't work

#option 3
import csv
from collections import defaultdict

columns = defaultdict(list)

with open('/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/fifa.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

print(columns) # don't work


#option 4 - panda
import pandas as pd 
my_csv = pd.read_csv('/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/fifa.csv', sep = ',')
print(my_csv)
print(my_csv[[' name',' rating']])

name_rating = my_csv[[' name', ' rating']]

name_rating_list = name_rating.values.tolist()
print(type(name_rating_list))
print(name_rating_list[0])

# extract only 1 column (string)
import pandas as pd 
my_csv = pd.read_csv('/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/fifa.csv', sep = ',')
print(my_csv)
print(my_csv[[' name']])

name_rating = my_csv[[' name']]

name_rating_list = name_rating.values.tolist()
print(type(name_rating_list))
print(name_rating_list)

# extract only 1 column (int)
import pandas as pd 
my_csv = pd.read_csv('/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/fifa.csv', sep = ',')
print(my_csv)
print(my_csv[[' rating']])

name_rating = my_csv[[' rating']]

name_rating_list = name_rating.values.tolist()
print(type(name_rating_list))
print(name_rating_list)