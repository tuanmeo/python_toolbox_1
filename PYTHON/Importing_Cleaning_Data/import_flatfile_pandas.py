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
# - data.head() --> check the first 5 rows of the dataframe,
# including the header 

# 4. Easily convert dataframe to numpy array by: data.values


#%%

# Using titanic.csv file
import pandas as pd
file = 'titanic.csv'
# Assign file name: file
file = pd.read_csv(file)