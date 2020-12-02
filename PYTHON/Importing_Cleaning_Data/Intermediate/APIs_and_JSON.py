# APIs: Application Programming Interface
# - Protocols and routines
#     - Building and interacting with software applications
#         - OMDb API (the Open Movie Database)
#     - Allows two software programs to communicate with each other

# Getting data from APIs through JSONS
# JSONs: JavaScript Object Notation
# - Real-time server-to-browser communication
# - Human readable not like picklefile

# LOAD JSONS IN PYTHON

# import json
# with open('snakes.json', 'r') as json_file:
#     json_file = json.load(json_file)

# Give the type dict to json_file
# to print use for loop:
#     for key, value in json_file.items():
#         print(key + ':', value)

#%%
# Loading and exploring a JSON
# Import the package
from io import StringIO
import json

from requests.api import request

# Load JSON: json_data using context manager
with open('a_movie.json') as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data:
for k in json_data.keys():
    print(k + ':', json_data[k]) #using dictionary[key] to access a value in dictionary

# %%
# CONNECTING TO AN API IN PYTHON
import requests
url = 'https://www.omdbapi.com/?t=hackers'
r = requests.get(url)
json_data = r.json() # return dict for json_data
for key, value in json_data.items():
    print(key + ':', value)
# %%
# WHAT WAS THAT URL?
# http: making an HTTP request
# www.omdbapi.com : querying the OMDB API
# ?t=hackers: 
#     ?: query string
#     t=hackers: ask the API return the movie with title (t): hackers

#%%
# API requests

# Pull some movie data down from the Open Movie Database (OMDB)
# Assign :
#   - variable url: 'http://www.omdbapi.com'
    # - Movie: The Social Network
    # - Query string: apikey=72bc447a&t=the+social+network

# Import requests package
import requests
import json
# Assign URL to variable: url
url = 'http://omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
print(type(r.text)) #--> give str type
# %%
# Convert .text to JSON from web
# apply json() method to the response object r and store the resulting dictionary in
# the variable json_data
json_data = r.json()

# Print each key-value pair in json_data
for key in json_data.keys():
    print(key + ':', json_data[key])
# %%
# THE WIKIPEDIA API
# find and extract information form the Wikipedia page for Pizza
# query will return nested JSONs (JSONs with JSONs) but Python
# will translate them into dic to dic
# The URL : https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza

# Import packages

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
for key, value in json_data.items():
    print (key + ':', value)

pizza_extract = json_data['query']['pages']['24768']['extract'] # holds the HTML of an extract from Wiki Pizza page as a string
print(pizza_extract)
# %%
