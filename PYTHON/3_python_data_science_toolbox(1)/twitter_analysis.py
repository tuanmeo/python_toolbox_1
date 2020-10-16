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
# use lambda function and filter() to select retweets
import pandas as pd
tweets_df = pd.read_csv('tweets.csv')
# Select retweets from the Twitter DataFrame: result
result = filter(lambda x:x[0:2] == 'RT', tweets_df['text'])
# Create list from filter object result: res_list
res_list = list(result)
# Print all tweet line by line
for i in res_list:
    print(i)
# %%
# Add try-except to function count_entries()
import pandas as pd
tweets_df = pd.read_csv('tweets.csv')

def count_entries(df, col_name = 'lang'):
    """Return a dictionary with counts of occurences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # add try block
    try:
        # extract column from DataFrame: col
        col = df[col_name]

        # iterate over the column in dataframe
        for i in col:
            # If i is in cols_count, add 1
            if i in cols_count:
                cols_count[i] = cols_count[i] + 1
            # else add i to cols_count, value = 1
            else:
                cols_count[i] = 1
        # return the cols_count dictionary
        return cols_count
    except TypeError:
        print('The DataFrame does not have a ' + col_name + ' column.')
    
# call count_entries(): result1
result1 = count_entries(tweets_df,'lang1')
print(result1)
for key, value in result1.items():
    print(key,":",value)

# %%
# Add raise ValueError to function count_entries()
import pandas as pd
tweets_df = pd.read_csv('tweets.csv')

def count_entries(df, col_name = 'lang'):
    """Return a dictionary with counts of occurences as value for each key."""
    # Add Raise ValueError to function
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # extract column from DataFrame: col
    col = df[col_name]

    # iterate over the column in dataframe
    for i in col:
        # If i is in cols_count, add 1
        if i in cols_count:
            cols_count[i] = cols_count[i] + 1
        # else add i to cols_count, value = 1
        else:
            cols_count[i] = 1
    # return the cols_count dictionary
    return cols_count
    
# call count_entries(): result1
result1 = count_entries(tweets_df,'lang1')
print(result1)
for key, value in result1.items():
    print(key,":",value)

# %%
