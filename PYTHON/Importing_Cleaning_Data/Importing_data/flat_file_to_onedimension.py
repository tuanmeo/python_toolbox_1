#%%
# Open the flat txt file (text of moby dick novel)
# Remember the process of open and close file 

file = open("moby_dick.txt", mode = 'r')

# Print file
print(file.read())

# Check whether file is closed
print(file.closed)

# close file
file.close()

# Check again whether file is closed
print(file.closed)


#%%
# Import text files line by line
# Want to print the first few lines 

# Concept of CONTEXT MANAGER: bind a variable 'file' by using context manager
# structure as with ... as ...
# the variable will be bound to function after with...

with open('moby_dick.txt', mode = 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# %%
# Import file MNIST.csv to numpy array
import numpy as np
import ast
import matplotlib.pyplot as plt
file1 = open('digits_MNIST_list.csv')
digits_MNIST = file1.read()
digits_MNIST1 = digits_MNIST.replace("'","")
digits = ast.literal_eval(''.join(digits_MNIST1))
digits_np = np.array(digits)
print(digits_np)

# appropriate method for convert list to numpy array
# Select and reshape a row
im = digits_np[21, 1:]
im_sq = np.reshape(im, (28,28))

# Plot reshaped data (matplotlib.pyplot required)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

# %%
# Import file digits.csv as datacamp
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable: file
file = 'digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28,28))

# Plot reshaped data (matplotlib.pyplot required)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

# %%
# For case has header (not need to import), delimiter not ',' could be '\t' for tab
# 'skiprows': allows to specify how many rows(not indices) wish to skip
# 'usecols' takes a list of the indices of the columns wish to keep

# np.loadtxt(): importing is tab-delimited, skip the first row, 
# import only the first and third columns

import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=(0,2))
print(data)

# %%
# Using file seaslug.txt
#   has a text header, consisting of strings
#   is tab-delimited

# Try to import it as-is using np.loadtxt() --> ValueError as "could not convert string to float"
# 2 solutions:
#   1. set the data type argument dtype = str(for string)
#   2. skip the first rows as skiprows

#%%
# use 1st method
import numpy as np
import matplotlib.pyplot as plt
file = 'seaslug.txt'

data = np.loadtxt(file,delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Plot a scatterplot of data
plt.scatter(data[:,0], data[:,1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

# %%
# Second method
import numpy as np
import matplotlib.pyplot as plt
file = 'seaslug.txt'
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:,0], data_float[:,1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()


# %%
# Working with mixed datatypes(1)
# datasets with various datatypes in different columns (string, float, etc)
#   - np.loadtxt() will freak out
#   - np.genfromtxt() can handle such structures, pass 'dtype=None' will figure
#     out what types each column should be

# Using titanic.csv for example:
#   + delimiter = ,
#   + argument 'names': True=header, False=no header
# Because the datatype are of different types, 'data' is an object called 
# a "structured array"
# Because numpy array have to contain elements that are all the same type,
# the structure array solves this by being a 1D array, where each element of
# the array is a row of the flat file imported.

# import the titanic file
file = 'titanic.csv'

import numpy as np
# import data by genfromtxt
data = np.genfromtxt(file,delimiter=',', names=True, dtype=None)

# print out the first 5 line of data, to get the ith row --> data[i]
print(data[0:5])

# Print out the column with name --> data['name'], print out the data of column 'Fare', 'Survived'
# Print out the last 4 values of 'survived' column
print(data['Survived'][-5:-1])
print(data['Survived'])

# Print out first 3 entries of data
print(data[:3])


# %%
# Another function is 'np.recfromcsv()' behaves similarly to 
# 'np.genfromtxt()', except that its default:
#   delimiter=','
#   names=True
#   dtype=None

# Using the function for 'titanic.csv' file, print the first 3 
# entries of the data

file = 'titanic.csv'
data = np.recfromcsv(file)

print(data[:3])
# %%
