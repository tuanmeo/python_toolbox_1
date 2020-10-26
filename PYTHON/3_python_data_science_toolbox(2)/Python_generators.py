#%%
# For large dataset, we use iterator to load to chunks
# also use generators function to load a file line by line
#   works on streaming data!
# Example of generator function

def num_sequence(n):
    """Generate values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1

result = num_sequence(10)
print(list(num_sequence(10)))
print(next(result))
# %%
