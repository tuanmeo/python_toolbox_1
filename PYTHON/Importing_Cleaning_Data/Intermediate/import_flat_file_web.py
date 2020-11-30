# IMPORT FLAT FILE FROM WEB
# 1. Download from web lead to:
#     - not reproducible, not scalable (take too much time to do it)

# 2. Learn how to:
#     - Import and locally save datasets from the web
#     - Load dataset into pandas DataFrames
#     - Make HTTP requests (GET requests)
#     - Scrape web data such as HTML
#     - Parse HTML into useful data (BeautifulSoup) 
#     - Use the urllib and requests packages

# 3. The urllib package:
#     - Provides interface for fetching data across the web
#     - urlopen(): accepts URLs instead of file names

#%% 
# Import required packages
# Import package: subpackage urllib.request
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE, responses
from typing import Protocol
from urllib.request import request, urlretrieve
from matplotlib.pyplot import locator_params
import pandas as pd
import matplotlib.pyplot as plt
from requests.models import Response
#%%
# IMPORTING FLAT FILES FROM THE WEB:
# - import 'winequality-red.csv' (contain physiochemical properties of red wine)
# - the url: 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# - load file into pandas DataFrame

# Assign url of file: url

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# save the file locally
urlretrieve(url, 'winequality-red-dl.csv')

# read file into pandas DataFrame and print its head
df = pd.read_csv('winequality-red-dl.csv', sep=';')
print(df.head())
# %%
# Open and read flat file from the web without saving 
# Using pd.read_csv()
# Plot fixed acidity (g(tartaric acid)/dm3) and count

# Read file into a DataFrame: df1
df1 = pd.read_csv(url, sep=';')

# Print the head of df1
print(df1.head())

# Plot first column of df
pd.DataFrame.hist(df1.iloc[:, 0:1]) # change .ix to iloc (for integer) and .loc for 'col_header'
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()


# %%
# IMPORT NOT-FLAT FILES FROM THE WEB
# url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# use pd.read_excel() to import an Excel spreadsheet
# print sheet names and print the head of the first sheet using its name, not its index 

# assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, sheet_name=None) # to import all sheets need to pass None to sheet_name

# Print all sheet names of xls
print(xls.keys()) # using .keys()to print the names of the sheets in Excel spreadsheet

# Print head of the first sheet using the sheet name, not the index of the sheet
print(xls['1700'].head())


# %%
# HTTP requests to import files from the web
# URL: Uniform/Universal Resource locator
# - References to web resources
# - Focus: web addresses <- focus on this 
# - Ingredients: 
#     - Protocol identifier: http:
#     - Resource name: such as datacamp.com

# HTTP: HyperText Transfer Protocol
# - Foundation of data communication for the web
# - Going to a website = sending HTTP request as:
#     - GET request
# - urlretrieve() performs a GET request

# How to get data from HTML: HyperText Markup Language

# GET requests using urllib

# extract the html from the wikipedia home page
# from urllib.request import urlopen, Request
# url = "https://www.wikipedia.org/"
# request = Request(url)
# response = urlopen(request) # send the request and catch the response 
# html = response.read() # restore html string to html variable
# response.close()

# GET requests using requests
# import requests
# url = "https://www.wikipedia.org/" 
# r = requests.get(url) # send and catch url
# text = r.text # return html as string

#%%
# Perform HTTP requests in Python using urllib
# Ping DataCamp servers to perform GET request to extract information
# from the first coding excerise
# "https://campus.datacamp.com/courses/1606/4135?ex=2"

# Import the functions urlopen and Request from the subpackage urllib.request

from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# Send the request and catch the response in the variable response
request = Request(url)
response = urlopen(request)

# Print the datatype of response
print(type(response))

# with a response http.client.HTTPResponse object, could read it to extract the HTML with read()
# Extract the response using the read() and store the result in the variable html
html = response.read()

# Print the html
print(html)

# Close the response!
response.close()

# %%
# Using REQUESTS package
# Using requests to ping "http://www.datacamp.com/teach/documentation" page.
# When using requests we don't have to close connection

# Import the package
import requests

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, sent the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)

# %%
# HTML
# - Mix of unstructured and structured data
# - Structured data:
#     - Has pre-defined data model, or
#     - Organized in a defined manner
# - Unstructured data: neither of these properties

# - To transform HTML to useful data need BeautifulSoup to:
#     - Parse and extract structured data from HTML

# BEAUTIFUL SOUP STRUCTURE:
# from bs4 import BeautifulSoup
# import requests
# url = "https://.../"
# r = requests.get(url)
# html_doc = r.text
# soup = BeautifulSoup(html_doc)
# print(soup.prittify())

# Using BeautifulSoup to prettify, extract the text and the hyperlinks from the url
# url = "https://www.python.org/~guido/"

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = "https://www.python.org/~guido/"

# package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)
# %%
# GETTING THE TEXT
guido_title = soup.title

# Print the title
print(guido_title)

# Extract the text from the HTML
guido_text = soup.get_text()

# Print out the text
print(guido_text)

# Getting the hyperlinks: a_tags
a_tags = soup.find_all('a') # hyperlinks are defined by the HTML tag <a>, pass to find_all without angel brackets

# The a_tags is a results set --> enumerate over it using for loop
for link in a_tags:
    print(link.get('href'))
# %%
