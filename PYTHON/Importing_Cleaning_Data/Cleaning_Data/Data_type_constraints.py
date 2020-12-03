# DATA TYPE CONSTRAINTS
#     - Text data: first name, last name, address... --> str
#     - Integers: # subscirbers, products sold...     --> int
#     - Decimals: temperature, $ exchange rates...    --> float
#     - binary: Is married, new customer, yes/no, ... --> bool
#     - Dates: order dates, ship dates,...            --> datetime
#     - Categories: marriage status, gender...        --> category

#%%
# Import packages


#%%
# Import csv sales file
sales = pd.read_csv('sales_example')
print(sales.head())
# %%
