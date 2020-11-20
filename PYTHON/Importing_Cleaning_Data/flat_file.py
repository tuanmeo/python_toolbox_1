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

# use 1st method
