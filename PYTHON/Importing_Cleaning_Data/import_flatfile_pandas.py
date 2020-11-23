# IMPORT FLAT FILES USING PANDAS

# 1. What a data scientist needs?
#   - Two dimensional labeled data structure(s)
#   - Columns of potentially different types
#   - Manipulate, slice, reshape, groupby, join, merge
#   - Perform statistics
#   - Work with time series data

# DataFrames are observations and variables

# 2. Manipulating pandas DataFrames
# - Exploratory data analysis
# - Data wrangling
# - Data reprocessing
# - Building models
# - Visualization

# 3. Importing using pandas
# - using pd.read_csv
# - sep = delimiter in numpy
# - comment='#'
# - na_values = takes a list of strings to recognize as NA/NaN
# - data.head() --> check the first 5 rows of the dataframe,
# including the header 

# 4. Easily convert dataframe to numpy array by: data.values


#%%

# Using titanic.csv file
import pandas as pd
file = 'titanic.csv'

# Assign file name: file
file = pd.read_csv(file)

# View the head of the DataFrame
print(file.head())

# %%
# Using pd.values to convert dataframe to numpy array
# Using 'digits.csv' file

import pandas as pd
file = 'digits.csv'

data = pd.read_csv(file, nrows=5, header=None)

# Convert to numpy array
data_array = data.values
 
# Print out type of data_array 
print(type(data_array))

# %%
# DEAL WITH FILE CONTAINED COMMENTS(#), MISSING VALUE (NA, NaN)
# Using 'titanic_corrupt.txt'
# sep='\t', comment='#', na_values='Nothing'
import pandas as pd
import matplotlib.pyplot as plt

file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')
    # for comment to remove any comment in data
    # 

# Print the head of the DataFrame
print(data.head()

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

# %%
data_array = data.values
print(data_array['Age'])
# %%
