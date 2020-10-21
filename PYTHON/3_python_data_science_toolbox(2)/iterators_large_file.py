#%%
# using pandas with chunk_size to load large data to comp
# example with csv file with 1 column has numbers, sum all the number
import pandas as pd
result = []

# using chunk_size to import data
for chunk in pd.read_csv('numbers.csv', chunksize=5):
    result.append(sum(chunk['x']))
total = sum(result)
print(total)
# %%
# if you don't want to store the result in a list then use this:
result = 0
for chunk in pd.read_csv('numbers.csv', chunksize=5):
    result += sum(chunk['x'])

print(result)
# %%
# working on tweets.csv in chunks of 10 
# initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize= 10):
    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)

#%%
# Put to a function with 3 variables: csv_file, c_size, and colname

def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of occurrences as value for each key."""
    counts_dict = {}

    for chunk in pd.read_csv(csv_file, chunksize = c_size):
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    return counts_dict

result = count_entries('tweets.csv', 10, 'lang')
print(result)
# %%
