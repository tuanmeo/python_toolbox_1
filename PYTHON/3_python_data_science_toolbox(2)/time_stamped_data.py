#%%
# Extract the time form time-stamped Twitter data
import pandas as pd
df = pd.read_csv('tweets.csv', index_col=0)

# Extract column created_at of df as tweet_clock_time
tweet_time = df['created_at']

# Extract the clock time (12th to 19th) as 11 to 19
tweet_clock_time = [entry[11:19] for entry in tweet_time]
print(type(tweet_clock_time))
# %%
