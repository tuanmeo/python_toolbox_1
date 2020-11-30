# APIs: Application Programming Interface
# - Protocols and routines
#     - Building and interacting with software applications
#         - OMDb API (the Open Movie Database)

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
import json

# Load JSON: json_data using context manager
with open('a_movie.json') as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data:
for k in json_data.keys():
    print(k + ':', json_data[k])
# %%
