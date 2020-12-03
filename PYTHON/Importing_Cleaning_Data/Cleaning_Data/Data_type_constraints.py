# DATA TYPE CONSTRAINTS
#     - Text data: first name, last name, address... --> str
#     - Integers: # subscirbers, products sold...     --> int
#     - Decimals: temperature, $ exchange rates...    --> float
#     - binary: Is married, new customer, yes/no, ... --> bool
#     - Dates: order dates, ship dates,...            --> datetime
#     - Categories: marriage status, gender...        --> category

#%%
# Import packages
import pandas as pd

#%%
# STRING TO INTEGERS
# Import csv sales file
sales = pd.read_csv('sales_example.csv')
print(sales.head())

# Print data type
print(type(sales))

# Print types of columns
print(sales.dtypes)

# Get DataFrame information
print(sales.info())

# Print sum of all Revenue column
print(sales['Revenue'].sum()) --> # give text because $ sign

# To sum revenue, need to remove $ sign, convert to int

sales['Revenue'] = sales['Revenue'].str.strip('$')
sales['Revenue'] = sales['Revenue'].astype('int')

# Verify type of 'Revenue'
assert sales['Revenue'].dtype == 'int' # return nothing for True, return error for False

print(sales['Revenue'].sum())
# %%

# %%
