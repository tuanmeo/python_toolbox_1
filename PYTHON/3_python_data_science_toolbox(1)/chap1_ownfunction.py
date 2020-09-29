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
