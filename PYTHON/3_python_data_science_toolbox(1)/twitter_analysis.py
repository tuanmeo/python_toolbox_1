# %%
# create function to return the result and call it
import pandas as pd
tweet_df = pd.read_csv('tweets.csv')
def count_entries(df,col_name = 'lang'):
    """Return a dictionary with counts of occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Extract column from DataFrame: col
    col = df[col_name]

#iterate over lang column in DataFrame
    for entry in col:
    #if lang is in lang_count, add 1:
        if entry in cols_count.keys():
            cols_count[entry] = cols_count[entry] + 1
    # else add lang to lang_count, set value to 1:
        else:
            cols_count[entry] = 1
    return cols_count

result = count_entries(tweet_df, 'lang')
result1= count_entries(tweet_df,'source')
print(result)
print(result1)
# %%
# Pass to flexible arguments
import pandas as pd
tweet_df = pd.read_csv('tweets.csv')
def count_entries(df,*args):
    """Return a dictionary with counts of occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Iterate over column names in args
    for col_name in args:
        # Extract column from DataFrame: col
        col = df[col_name]

    #iterate over lang column in DataFrame
        for entry in col:
        #if lang is in lang_count, add 1:
            if entry in cols_count.keys():
                cols_count[entry] = cols_count[entry] + 1
        # else add lang to lang_count, set value to 1:
            else:
                cols_count[entry] = 1
    return cols_count

result = count_entries(tweet_df, 'lang')
result1= count_entries(tweet_df,'lang','source')
print(result)
print(result1)
# %%
# print dictionary as line by line
# Iterate over key/value pairs in dict and print them
for key, value in result1.items():
    print(key, ":", value)
# %%
