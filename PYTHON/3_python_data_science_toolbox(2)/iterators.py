#%%
for i in range(4):
    print(i)
# %%
# Iterating over iterables(1)
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# iterating over the list by using for loop, use person as variable
for person in flash:
    print(person)

# %%
# Create an iterator for flash: superhero
superhero = iter(flash)
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))
# %%
# iterables with range()
# range() creates a range object with an iterator that produces the values
# until it reaches the limit. Range() doesn't create a list.
# If range() created the actual list, call it with a value of 10^100 will
# crash the memory of computer. Test it!!!

number1 = iter(range(4))
print(next(number1))
print(next(number1))
print(next(number1))

# test with 10**100 iterator
googol = iter(range(10**100))
print(next(googol))
print(next(googol))
print(next(googol))
# still work so that it is not a list
# %%
# iterators as function arguments
# create range object from 10 to 20 as values
values = range(10,21)
# change to list
values_list = list(values)
# cal sum of all values in 
values_sum = sum(values)
print(values_sum)
# %%
