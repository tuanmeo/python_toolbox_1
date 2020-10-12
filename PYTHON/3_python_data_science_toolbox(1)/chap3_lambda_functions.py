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
# use function 'reduce' from functools module
# reduce is useful for 'map' and 'filter' returns a single
# value as a result.

from functools import reduce
# create a list of strings:
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
# Use reduce() to apply a lambda over stark
result = reduce(lambda item1, item2 : item1 +" " + item2, stark)
print(result)
# %%
# or create own function
def put_together(*args):
    """concatenate strings in args together"""
    all_string = ''
    for word in args:
        all_string += word
    return all_string
put_together('robb', 'sansa')

print(''.join(stark))
# %%
def put_together(x):
    """concatenate strings in args together"""
    all_string = ''
    for word in x:
        all_string += word
    return all_string
put_together(stark)
# %%
# Apply lambda and try-except function
# wirte a lambda function and use filter() to select retweets, tweets begin with 'RT'
import pandas as pd
tweets = pd.read_csv('tweets.csv')

tweets_text= tweets['text']

result = filter(lambda x:x[0:2] == "RT",tweets_text)
# print all result as list as line by line
for i in list(result):
    print(i)
# %%
# add try-except to count_entries() function
def count_entries(df, col_name = 'lang'):
    """Return a dictionary with counts of occurrences as value for each key."""
    cols_count = {}
    #add try block
    try:
        # extract column from DataFrame: col
        col = df[col_name]
        # iterate over the column name in dataframe
        for entry in col:
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
        # return the cols_count dictionary
        return cols_count
    #add the except block
    except TypeError:
        print('The DataFrame does not have a ' + col_name + ' column.')

result1 = count_entries(tweets, 'lang')
for i,y in result1.items():
    print(i, ':', y)
# %%
