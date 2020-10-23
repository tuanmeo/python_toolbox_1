#%%
# Using enumerate(), data
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

#%%
# Create a list of tuples, mutant_list
mutant_list = list(enumerate(mutants,start = 1))
print(type(mutant_list))
print(mutant_list)
# %%
# using for loop by unpacking the tuples, starting index at 1
for index1, value1 in enumerate(mutants, start = 1):
    print(index1, value1)

# %%
# Using zip()
# create a list of tuples from 3 lists above as order, mutant_data
mutant_data = list(zip(mutants, aliases, powers))
print(mutant_data)

# %%
# Using zip() and for loop
mutant_zip = zip(mutants, aliases, powers)
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)
print(type(mutant_zip))
# %%
# because no function to 'unzip' for doing the reverse of what 'zip' does.
# we can use * in zip as example:
z1 = zip(mutants, powers)
# unzip the tuples in z1 by unpacking with * and zip():
result1, result2 = zip(*z1)

print(result1)
print(result2)
# %%
