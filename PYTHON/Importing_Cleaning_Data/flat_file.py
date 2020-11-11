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
