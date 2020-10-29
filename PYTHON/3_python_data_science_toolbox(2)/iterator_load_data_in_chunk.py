#%%
# Create an iterable reader object (can use next() on it)
# Read file in small chunk with read_csv()
# Use data from world_ind_pop_data.csv to extract CountryName, Urban population (% of total)
import pandas as pd
world_bank = pd.read_csv('world_ind_pop_data.csv')

world_bank_ind_pop = world_bank[['CountryName','Urban population (% of total)']]
print(world_bank_ind_pop)

# Export to csv file 
world_bank_ind_pop.to_csv(r'C:\Test_git\python_toolbox_1\PYTHON\3_python_data_science_toolbox(2)\world_ind_pop.csv',index=False)


# %%
# Read world_bank_ind_pop.csv in small DataFrame chunks (size = 100)

# Initialize reader object: df_reader
df_reader = pd.read_csv('world_ind_pop.csv', chunksize= 100)

# Print two chunks
print(next(df_reader))
print(next(df_reader))


# %%
# Import world_ind_pop_data.csv to chunksize 1000

# Initialize reader obj: urb_pop_reader
urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize= 1000)

# Get the first DataFrame Chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
# wrap condition in [[]] to filter all entries pass the condition

# Create list of tuples fro the zip obj (2 columns)
# Zip DataFram columns of interest: pops 
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])
# Turn zip obj into list: pops_list
pops_list = list(pops)

#print out
print(pops_list)


# %%
# Adding a column to a DataFrame, which product of total population and urban population(%)
# as Total Urban Population
# Use list comprehension to create new DataFrame Column
df_pop_ceb['Total Urban Population'] = [(int(value[0])*int(value[1])*0.01) for value in pops_list]

print(df_pop_ceb)
# %%
# Write a list comprehension to generate a list as 'Total Urban Population'
# 'Total Urban Population' should only be able to take on integer values
# ensure to cast the output expression to an integer with int()
# Create a scatter plot where x = 'Year', y = 'Total Urban Population'

# Initialize reader obj: urb_pop_reader
urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize= 1000)

# Get the first DataFrame Chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
# wrap condition in [[]] to filter all entries pass the condition

# Create list of tuples fro the zip obj (2 columns)
# Zip DataFram columns of interest: pops 
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])
# Turn zip obj into list: pops_list
pops_list = list(pops)
print(pops_list)
# use list comprehension to create new column 'Total Urban Population' in dataframe
df_pop_ceb['Total Urban Population'] = [int(pop[0]*pop[1]*0.01) for pop in pops_list]

# Plot urban population data
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
df_pop_ceb.plot(kind='scatter', x ='Year', y ='Total Urban Population')
plt.show()



# %%
# Requirement: plot the data include 'Year' and 'Total Urban Population' of 'world_ind_pop_data.csv'
# using chunksize of 1000 for entire dataset
import pandas as pd
import matplotlib.pyplot as plt
# step_1: open csv file with chunksize = 1000
world_bank_data = pd.read_csv('world_ind_pop_data.csv', chunksize = 1000)

# step_2: create empty dataframe: data
data = pd.DataFrame()

# Step_3: iterate over each dataframe chunk
for df_urb_pop in world_bank_data:
    
    # select the CountryCode = 'CEB'
    df_urb_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
    #Zip the column 'Total Population' and 'Urban population (% of total)': pops
    pops = zip(df_urb_ceb['Total Population'], df_urb_ceb['Urban population (% of total)'])
    # --> create a list of lists 
    pops_list = list(pops)

    # Add new column in DataFrame: Total Urban Population
    # use list comprehesion to create new column with calculation itself
    df_urb_ceb['Total Urban Population'] = [int(pop[0]*pop[1]*0.01) for pop in pops_list]

    # Append DataFrame chunk to data: data
    data = data.append(df_urb_ceb)

data.plot(kind='scatter',x='Year',y='Total Urban Population')
plt.show()

print(list(world_bank_data))
# %%
