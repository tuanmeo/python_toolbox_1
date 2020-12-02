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