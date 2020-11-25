# OTHER FILE TYPES
# - Excel spreadsheets
# - MATLAB Files
# - SAS files
# - Stata files
# - HDF5 files

# PICKLED FILES
# - file type native to Python
# - Motivation: many datatypes for which it isn't obvious how to store them
# - Pickled files are serialized, serials for merely importing to computer serialize means converting object to bytestream
# - import pickle for 'rb' - readable bynary, file only readable computer not human
# - number of types data as lists, dictionaries are difficult to store as flat file.
# - JSON is appropriate for dictionaries type.



# IMPORT EXCEL FILES

# - Figure sheet names as data.sheet_names
# - Call the specific sheet name by function data.parse('sheetname'), or data.parse(0)--> index the first column
# - In parse function can add:
#       - skiprows
#       - names --> change the name of columns
#       - usecols
#%%
# Explore current directory 
! ls
# %%
# Explore current directory by native python
import os
wd = os.getcwd()
os.listdir(wd)

# %%
# IMPORT PICKLE FILE
# Using data.pkl file to excercise the data in objective (not to read)

import pickle
# Open data as file
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)
    print(d)
    print(type(d))


# %%
# IMPORT EXCEL FILE
# Using 'battledeath.xlsx' file 

import pandas as pd
file = 'battledeath.xlsx'

# Load excel file xls
xls = pd.ExcelFile(file)
print(xls.sheet_names)


# %%
# Import excel file --> 'battledeath.xlsx'
# follow the xls file above, import sheet '2004'
# Import sheet by name column
df1 = xls.parse('2004')
print(df1.head())
# %%
# Import sheet by index
df2 = xls.parse(0)
print(df2.head())
# %%
# Parse the first col using index
# skip the first row
# name the column 'Country' and 'AAM due to War (2002)'
# The value passed to skiprows and names all need to be of type 'list'

df1 = xls.parse(0,skiprows=1, names=('Country', 'AAM due to War (2002)'))
print(df1.head())
# %%
# Parse the first col using index, sheet 2
# skip the first row
# Rename the column 'Country'
# parse only the first column
# The value passed to skiprows, names, and usecols all need to be of type 'list'
df2 = xls.parse(0,usecols=[0], skiprows=1, names=['Country'])
print(df2.head())
# example for choosing 2 columns
df3 = xls.parse(1, usecols=[0,1], skiprows=1, names=['Country','death'])
# Select 2 columns, change names must be 2 fields
print(df3.head())


# %%
# SAS and STATA files
# SAS: Statistical Analysis System: analytics and biostatistics
# Stata: academic social sciences research

# Import file 'sales.sas7bdat', save file as pandas DataFrame

# Import lybraryies requirements
import pandas as pd
import matplotlib.pyplot as plt

# Import module SAS7BDAT from the library sas7bdat
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features, hist
pd.DataFrame.hist(df_sas[['P']]) # for [['P']] --> for changing series to dataframe
plt.ylabel('count')
plt.show()

# %%
# Import 'disarea.dta' file by pandas

# Load STATA file to a DataFrame: df
df = pd.read_stata('disarea.dta')
# Print the head of df
print(df.head())
# Print out the head of the 'wbcode' column
print(df['wbcode'].head())

# Plot histogram of one column of df
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of Countries')
plt.show()


# %%
# IMPORT HDF5 FILE
# import package h5py
import numpy as np
import h5py

# Assign file name: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print data type of data
print(type(data))

# Print the keys of data
for key in data.keys():
    print(key)

# Extract data from hdf5, strain

# Get the HDF5: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain']
# Set number of time points to sample: num_samples
num_samples = 10000
# Set time vector
time = np.arange(0,1,1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS time (s)')
plt.ylabel('Strain')
plt.show()

# %%
# IMPORT MATLAB FILE
# SciPy to read and load
# scipy.io.loadmat() - read .mat files
# scipy.io.savemat() - write .mat Files

# - class 'dict'
#     keys = MATLAB variable names
#     values = objects assigned to variables

# Using file 'albeck_gene_expression.mat'
# Print type() of mat

# Import scipy package
import scipy.io
import matplotlib.pyplot as plt
# Load mat file as: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print type of mat
print(type(mat))
# %%
# Print the keys of the MATLAB dictionary
print(mat.keys()) # key words not begin with __ or end with __ are objectives

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the values corresponding to the key 'CYratioCyt'
print(mat['CYratioCyt'].shape)
array1 = mat['CYratioCyt'] # (200,137) --> 200 line with 137 values each

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:] # from line 25, start at value 5th to all
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()

# Print the type of the value corresponding to the key 'CYratioCyt'
# %%
