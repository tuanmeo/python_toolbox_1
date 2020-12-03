# TWITTER API AND AUTHENTICATION
#     How to stream data from the Twitter API
#     How to filter incoming tweets for keywords
#     About API Authentication and OAuth
#     How to use the Tweepy Python package

# Access the Twitter API:
#     - had account
#     - Various APIs: 
#         - REST API: provide programmatic access to read and write twitter data. Author a 
#                     new tweet, read author profile and follower data, and more.
#                     Identifies Twitter applications and users using OAuth; responses are
#                     available in JSON.
#         - Streaming API: Monitor or process Tweets in real-time, give developers low latency
#                         access to Twitter's global stream of Tweet data. A proper implementation
#                         of a streaming client will be pushed messages indicating Tweets and 
#                         other events have occurred, without any of the overhead associated
#                         with polling a REST endpoint.
#                         If conducting singular searches, read user profile info, or post 
#                         Tweets, consider using the REST API

#                         Several streaming endpoints:
#                         - Public streams: streams of public data flowing through Twitter.
#                                         Suitable for following specific users or topics, 
#                                         and data mining.
#                         - User steams: single-user streams, containing roughly all of the 
#                                         data corresponding with a single user's view of Twitter

#                         - Site streams: the multi-user version of user streams. Site streams are
#                                         intended for servers which must connect to Twitter on 
#                                         behalf of many users.

#         - for public streams:
#             - GET statuses/sample: Returns a small random sample of all public statuses.
#                                     The Tweets returned by the default access level are 
#                                     the same, so if two different clients connect to this
#                                     endpoint, see the same Tweets.
#                                     Resource URL: https://stream.twitter.com/1.1/statuses/sample.json
#             - Firehose: Return all public statuses. Require level of access and money.
            
#     - log to apps.twitter.com -> create new app
#     - go to Keys and Access Tokens --> copy:
#         API Key
#         API Secret
#         Access token
#         Access Token secret

#     - Using Tweepy: Authentication handler to stream Twitter data
#     import tweepy, json
#     access_token = "..."
#     access_token_secret = "..."
#     consumer_key = "..."
#     consumer_secret = "..."
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)

#     - Define stream listener class
#     class MyStreamListener(tweepy.StreamListener):
#         def __init__(self, api=None):
#             super(MyStreamListener, self).__init__()
#             self.num_tweets = 0
#             self.file = open("tweets.txt", "w")
#         def on_status(self, status):
#             tweet = status.json
#             self.file.write(json.dumps(tweet) + '\\n')
#             tweet_list.append(status)
#             self.num_tweets += 1
#             if self.num_tweets < 100:
#                 return True
#             else:
#                 return False
#             self.file.close()

#     --> define MyStreamListener create tweets.txt collected tweets and wrote in.
#         when 100 streams will close and stop the listner

#     - Create Streaming object and authenticate
#     l = MyStreamListener()
#     stream = tweepy.Stream(auth, l)
#     - This line filters Twitter Streams to capture data by keywords:
#     steam.filter(track=['apples', 'oranges'])

# API Authentication

#%%
# Import required packages
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
#Load and explore Twitter data offline
# Read the Twitter data into a list: tweets_data
# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connnection to file
tweets_file = open(tweets_data_path, 'r')

# Read in tweets and store in list: tweets_data
for line in tweets_file: #load each tweet to a variable line
    tweets = json.loads(line)
    tweets_data.append(tweets)

# Close the connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())
# %%
# Extract Twitter data to DataFrame
# Build DataFrame of tweet texts and languages

df = pd.DataFrame(tweets_data, columns=('text', 'lang'))
print (df.head())


# %%
# Analyze to count how many tweets contain the words:
    # cliton
    # trump
    # sanders
    # cruz

# Define function word_in_text(): tell us whether the first argument
# (a word) occurs within the 2nd argument (a tweet)

import re
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

# Iterate over the rows of the DataFrame and cal how many tweets contain each of our keywords
# The list of objects for each candidate has been initialized to 0

# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned

for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text']) # increases the value of clinton by 1 each time a tweet(text row) mentioning 'Clinton' is encountered.
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

#%% 
# PLOTTING TWITTER DATA 
# Plot bar chart using statistical data visualization library seaborn
# import seaborn as sns
# construct a barplot using sns.barplot, passing it 2 arguments:
    # - a list of labels and
    # - a list containing the variables you wish to plot (clinton, trump and so on)

# import packages matplotlib.pyplot and seaborn
# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels: cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot the bar chart
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel='count')
plt.show()
# %%
