#%%
# create square root function

def square_root(x):
    value = x **0.5
    return value

square_root(4)
# %%
# Using LAMBDA for Anomymous functions
raise_to_power = lambda x, y: x ** y
raise_to_power(2,4)
# %%
# Map function
# map(func,seq) -- applies function to ALL elements in the sequence
# we can use Lambda without naming the function

nums = [48, 6, 9, 21, 1]

square_all = map(lambda num: num ** 2, nums)
print(list(square_all))

# %%
# create function add !!! to string a
add_bangs = lambda x: x + "!!!"
add_bangs("a")
# %%
# create function to concatenate echo copies of word1
def echo_word(word1, echo):
    """Concatenate echo copies of word1"""
    words = word1 * echo
    return words

echo_word('tuan dep trai ', 3)
# %%
# create echo_word with lambda
echo_word_lam = lambda word1, echo: word1 * echo
echo_word_lam('tuan dap chai', 3)
# %%
# using Map() with Lambda
spells = ["protego", "accio", "expecto patronum", "legilimens"]
# use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + "!!!", spells)
print(list(shout_spells))
# %%
# apply Lambda in filter() function to sort with condition
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 
                'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

result = filter(lambda mem: len(mem) > 6, fellowship)
print(list(result))

# %%
# create function to filter 
for i in fellowship:
    print(len(i))
# %%
