#%%
# Data sources can be so large in size to store the entire dataset in memory
# process the first 1000 rows of a file line by line
# create a dictionary of the counts of how many times each country appears in a column in the dataset

# open a connection to the file to ensure that resources are efficiently 
# allocated when opening a connection to a file

with open('world_ind_pop_data.csv') as file:
    
    # skip the column name
    file.readline()
    line = file.readline().split(',')
    print(line)
# %%
