#%%

# change from [1,2,3] csv to a list
# import using csv
import csv
import numpy as np
filepath = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/baseball_height_in.csv'
file = open(filepath)
reader = csv.reader(file)
data = list(reader)
data = sum(data,[])
print(data)
data = [int(i) for i in data]
print(data)

# change to array for calculating
np_data = np.array(data)
print(type(np_data))
print(np_data)
# %%
# import list of lists to python using ast
import ast
str = "[[0,0,0],[0,0,1],[1,1,0]]"
lists = ast.literal_eval(str)
print(lists)
# %%
# import list of lists (integer) to python
import ast
filepath_3 = '/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Introduction_Python/baseball_heightin_weightpound.csv'
file_3 = open(filepath_3)
baseball = file_3.read().splitlines()
baseball_1 = ast.literal_eval( ''.join(baseball))

print(baseball_1)
print(type(baseball_1))

#For tuples
#>>> ast.literal_eval('[(0,0,0), (0,0,1), (1,1,0)]')
#[(0, 0, 0), (0, 0, 1), (1, 1, 0)]



#%%
# For case of [['0','1','2'], ['3','4','5']] change to numpy array 
# import file from datacamp MNIST digit: 
# file = 'file name'
# data = open(file)
# reader = csv.reader(data) <-- use import csv
import ast
import numpy as np
file = open('digits_mni.csv')
digits_raw = file.read()
digits = digits_raw.replace("'","")
digits1 = ast.literal_eval(''.join(digits))
digits_np = np.array(digits1)
print(digits_np)
#%%
 # import 191, 184, 185, 180, 181, to a list
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


#%%
# import a list of string in python
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



# %%
# import list of lists to pandas dataframe
import pandas as pd
data = [['New York Yankees', 'Acevedo Juan', 900000, 'Pitcher'], 
        ['New York Yankees', 'Anderson Jason', 300000, 'Pitcher'], 
        ['New York Yankees', 'Clemens Roger', 10100000, 'Pitcher'], 
        ['New York Yankees', 'Contreras Jose', 5500000, 'Pitcher']]

df = pd.DataFrame.from_records(data)
print(df)
# %%
# Use transposing data
import pandas as pd
data = [['New York Yankees', 'Acevedo Juan', 900000, 'Pitcher'], 
        ['New York Yankees', 'Anderson Jason', 300000, 'Pitcher'], 
        ['New York Yankees', 'Clemens Roger', 10100000, 'Pitcher'], 
        ['New York Yankees', 'Contreras Jose', 5500000, 'Pitcher']]
df = pd.DataFrame(data, columns=["Team", "Player", "Salary", "Role"])
print(df)
# %%

import pandas as pd
data = [['New York Yankees', 'Acevedo Juan', 900000, 'Pitcher'], 
        ['New York Yankees', 'Anderson Jason', 300000, 'Pitcher'], 
        ['New York Yankees', 'Clemens Roger', 10100000, 'Pitcher'], 
        ['New York Yankees', 'Contreras Jose', 5500000, 'Pitcher']]

data = pd.DataFrame(data)
print(data)
# %%
import pandas as pd

data = [['key1', 'key2', 'key3', 'key4'], 
    ['New York Yankees', 'Anderson Jason', 300000, 'Pitcher'], 
    ['New York Yankees', 'Clemens Roger', 10100000, 'Pitcher'], 
    ['New York Yankees', 'Contreras Jose', 5500000, 'Pitcher']]

data = pd.DataFrame(data[1:], columns=data[0])
print(data)
# %%
