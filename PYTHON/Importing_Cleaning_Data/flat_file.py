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


# %%
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

# appropriate method for list

# Select and reshape a row
im = digits_np[21,1:]
im_sq = np.reshape(im, (28,28))

# Plot reshaped data (matplotlib.pyplot)
plt.imshow(im_sq, cmap = 'Greys', interpolation='nearest')
plt.show()

# %%
