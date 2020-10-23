#%%
#Using data of world bank
import pandas as pd
df = pd.read_csv('world_ind_pop_data.csv')
print(df)
# %%
columns_name = df.head(0)
for name in columns_name:
    print(name)
# %%
# Create feature_names and row_vals
feature_names = ['CountryName', 'CountryCode', 'IndicatorName', 'IndicatorCode', 'Year', 'Value']
row_vals = ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']

# assign to zipped_lists
zipped_lists = zip(feature_names, row_vals)
# Create dict from zip obj by call dict()
rs_dict = dict(zipped_lists)
print(rs_dict)
# %%
# Create a list from DataFrame
print(list(columns_name))


# %%
# for conveniency in repeat the process, create a function lists2dict()

def lists2dict(list1, list2):
    """Return a dictionary where list1 = keys and list2 = values."""
    zipped_list = zip(list1, list2)
    dicted_zip = dict(zipped_list)
    return dicted_zip

# call list2dict as rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)
print(rs_fxn)


# %%
# Use a list comprehension to generate a list of dicts, where 
# keys = header names and values = row entries
import ast
file = open('world_bank_info.csv')
file1 = file.read().splitlines()
world_bank = ast.literal_eval( ''.join(file1))

# Print the first 2 lists in row_lists
print(world_bank[0])
print(world_bank[1])

# Turn lists of lists into list of dicts: list_of_dicts
# use list comprehension create dict with keys: feature_names, values world_bank lists

list_of_dicts = [lists2dict(feature_names,entry) for entry in world_bank]

# print the first 2 dicts in lists_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])


# %%
# Convert a list of dictionaries into a pandas DataFrame by using
# DataFrame()

df = pd.DataFrame(list_of_dicts)
print(df.head(2))
# %%
