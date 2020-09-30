#%%
# create a dictionary of lang and numbers of given langs
import pandas as pd
df = pd.read_csv('tweets.csv')
lang_count = {}

col = df['lang']

#iterate over lang column in DataFrame
for index in col:
    #if lang is in lang_count, add 1:
    if index in lang_count.keys():
        lang_count[index] = lang_count[index] + 1
    # else add lang to lang_count, set value to 1:
    else:
        lang_count[index] = 1

print(lang_count)
# %%
# create function to return the result and call it
tweet_df = pd.read_csv('tweets.csv')
def count_entries(df,col_name):
    lang_count = {}

    col = df[col_name]

#iterate over lang column in DataFrame
    for entry in col:
    #if lang is in lang_count, add 1:
        if entry in lang_count.keys():
            lang_count[entry] = lang_count[entry] + 1
    # else add lang to lang_count, set value to 1:
        else:
            lang_count[entry] = 1
    return lang_count

result = count_entries(tweet_df, 'lang')
print(result)
# %%
# change value of variable in global
team = "teen titans"

def change_team():
    """Change the value of the global variable team."""
    global team
    team = "justice league"
print(team)
change_team()
print(team)
# %%
# Nested functions
# Not useful for too much variables
def mod2plus5(x1, x2, x3):
    """Returns the remainder plus 5 of three values"""
    new_x1 = x1 % 2 + 5
    new_x2 = x2 % 2 + 5
    new_x3 = x3 % 2 + 5

    return (new_x1, new_x2, new_x3)

print(mod2plus5(3,5,7))

# use nested functions 

def mod2plus5 (x1, x2, x3):
    """Returns the remainder plus 5 of three values"""
    def inner(x):
        """Returns the remainder plus 5 of a value"""
        return x % 2 + 5
    return (inner(x1), inner(x2), inner(x3))

print (mod2plus5(3,5,7))
# %%
# remember the value of function

def raise_val(n):
    """Return the inner function."""

    def inner(x):
        """Raise x to the power of n."""
        raised = x ** n
        return raised
    return inner

square = raise_val(2)
print(square(3))
# %%
# create function three_shouts()

def three_shouts(x1,x2,x3):
    """Returns a tuple of strings concatenated with '!!!'."""
    def inner(x):
        """Return a string concatenated with '!!!'."""
        return x + '!!!'
    return (inner(x1), inner(x2), inner(x3))

print(three_shouts('a', 'b', 'c'))
 
# %%
def echo(n):
    """Concatenate n copies of word1."""
    def inner_echo(word1):
        echo_word = word1 * n
        return echo_word
    return inner_echo

# call echo twice
twice = echo(2)
# call echo thrice
thrice = echo(3)

print(twice('hello'), thrice('hello'))

# %%
# Use keyword nonlocal
def echo_shout(word):
    """Change the value of a nonlocal variable."""
    # Concatenate word with itself: echo_word
    echo_word = word * 2
    # Print echo_word
    print(echo_word)
    # define inner function shout()
    def shout():
        """ Alter a variable in the enclosing scope."""
        nonlocal echo_word
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    # call the function shout
    shout()
    # print echo_word
    print(echo_word)

echo_shout('hello')
# %%
# Add a default argument

def power(x, y = 1):
    value = x ** y
    return value

result1 = power(2,2)
result2 = power(2)
print(result1)
print(result2)
# %%
# Flexible argurments: *args(1)
def add_all(*args):
    """Sum all values in *args together."""
    # initialize sum
    sum_all = 0
    # accumulate the sum
    for num in args:
        sum_all += num # sum all the value in tuple
    return sum_all

add_all(1,5)
# %%
# print out key and value of dictionary use **kwargs
def print_all(**kwargs):
    """Print out key-value pairs in **kwargs."""
    # print out the key-value pairs
    for key, value_1 in kwargs.items():
        print("%s = %s" %(key,value_1))
print_all(name = "tuan nguyen", key = "freelance")
# %%
# Concatenate echo copies of word1 and three !!!
# default argument = 1

def shout_echo(word1, echo = 1):
    """Concatenate echo copies of word1 and !!!."""
    echo_word = word1 * echo + "!!!"
    return echo_word

no_echo = shout_echo('Hey')
with_echo = shout_echo('Hey', 5)
print(no_echo)
print(with_echo)

# %%
def shout_echo(word1, echo = 1, intense = False):
    """Concatenate echo copies of word1 and !!!."""
    echo_word = word1 * echo + "!!!"
    if intense is True:
       echo_word = echo_word.upper()
    else:
        echo_word = echo_word
    return echo_word
with_big_echo = shout_echo('Hey',5,True)
with_no_echo = shout_echo('Hey',intense = True)

print(with_big_echo)
print(with_no_echo)
# %%
# Define function 'gibberish()' which can accept a variable number of 
# string values. Its return value is a single string composed of all
# the string arguments concatenated together in the order they were 
# passed to the function call.

def gibberish(*args):
    """Concatenate strings in *args together."""
    # Initialize an empty string: hodgepodge
    hodgepodge = ""
    for word in args:
        hodgepodge += word
    return hodgepodge

text = gibberish("a", "b", "c", "d")
print(text)
# %%
# define a function that accepts a variable number of keyword arguments.
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        #Print out the keys and values, separated by :
        print(key + ":" + value)
    print("\nEND REPORT")

#first call
report_status(name = 'luke', affiliation = 'jedi', status = 'missing')
report_status(name = 'anakin', affiliation = 'sith lord', status = 'deceased')
# %%
