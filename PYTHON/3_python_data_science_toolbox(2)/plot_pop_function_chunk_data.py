#%%
# Define function plot_pop() which takes 2 arguments: 
# 1. The filename of the file to be processed
# 2. the country code of the rows to process in dataset

# The function will do:
# - Loading of the file chunk by chunk
# - Creating the new column of urban population values
# - Plot the urban population data

# %%
# Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Create function plot_pop()
def plot_pop(filename,country_code):

    # Loading file to chunk by chunk
    world_bank = pd.read_csv(filename,chunksize=1000)
    # Create empty DataFrame: data
    data = pd.DataFrame()
    # Iterate over each dataframe chunk
    for df_urb_pop in world_bank:
        # select the CountryCode
        df_urb_code = df_urb_pop[df_urb_pop['CountryCode'] == country_code]
        # zip two column 'Total Population' and 'Urban poplulation (% of total)'
        pops = zip(df_urb_code['Total Population'],
                   df_urb_code['Urban population (% of total)'])
        # change zip to list
        pops_list = list(pops)
        
        # Add new column to df_urb_pop: total_urban_population, using list comprehesion
        df_urb_code['Total urban population'] = [int(num[0]*num[1]*0.01) for num in pops_list]
        # Append DataFrame chunk to data: data
        data = data.append(df_urb_code)

    
    data.plot(kind='scatter',x='Year', y='Total urban population')
    plt.show()

fn = 'world_ind_pop_data.csv'
plot_pop(fn,'CEB')
plot_pop(fn,'ARB')
# %%
