#%%
# Data sources can be so large in size to store the entire dataset in memory
# process the first 1000 rows of a file line by line
# create a dictionary of the counts of how many times each country appears in a column in the dataset

# open a connection to the file to ensure that resources are efficiently 
# allocated when opening a connection to a file

with open('world_ind_pop_data.csv') as file:
    
    # skip the column name
    file.readline()

    #Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for i in range(0,1000):
        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        
        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
for i,j in counts_dict.items():
    print(i,j)
# %%
# Create a function to limit and calculate the data as dataframe
import pandas as pd
world_bank = pd.read_csv('world_ind_pop_data.csv')

def count_countries(num,df,col_name = 'CountryName'):
    """Return number of countries in df."""
    # Limit the data
    world_bank_limit = world_bank.iloc[:num]

    # Initialize empty list
    counts_dict_df = {}
    # Extract column from DF:
    col = world_bank_limit[col_name]
    for i in range(0,1000):
        for entry in col:
            if entry in counts_dict_df.keys():
                counts_dict_df[entry] += 1
            else:
                counts_dict_df[entry] = 1
        return counts_dict_df        

result = count_countries(1000,world_bank,'CountryName')
print(result)
# %%
  # Test without using function and list comprehensions
  
    # Initialize empty list
    counts_dict_df = {}
    # Extract column from DF:
    limit_data = world_bank.iloc[:1000]
    col = limit_data['CountryName']        
    for entry in col:
        if entry in counts_dict_df.keys():
            counts_dict_df[entry] += 1
        else:
            counts_dict_df[entry] = 1

print(counts_dict_df)



# %%
# GENERATOR TO LOAD DATA IN CHUNKS
# use GENERATORS to process entire file as "lazily evaluate data"
# yielding only chunks of data at a time instead of the whole thing at once.
# Define a generator function 'read_large_file()' that produces a 
# generator object which yields a single line from a file each time
# next() is called on it.

# Define read_large_file()
def read_large_file(file_obj):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_obj.readline()
        # Break if this is the end of the file
        if not data:
            break
        # Yield the line of data
        yield data

# Open a connection to the file
with open('world_ind_pop_data.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first 3 lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

# %%
file = open('world_ind_pop_data.csv')
print(list(file))

# %%
