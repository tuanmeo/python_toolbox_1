# THE RELATIONAL MODEL
# - Each row or record in a table represents an instance of an entity type
# - Each column in a table represents an attribute or feature of an instance
# - Every table contains a primary key column, which has a unique entry for each row
# - There are relations between tables



# CREATING A DATABASE ENGINE
# - SQLite database
#     - Fast and Simple
# - SQLAlchemy
#     - Works with many Relational Database Management Systems
#     - Structure:
#         from sqlalchemy import create_engine
#         engine = create_engine('sqlite:///Northwind.sqlite')

# - Getting table names
#     - engine.table_names()


#%%
# CREATING A DATABASE ENGINE
# Create an engine to connect to the SQLite database 'Chinook.sqlite'
# create_engine('sqlite://Chinook.sqlite')

# Import necessary module
from pandas.core.frame import DataFrame
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save a table names as a list: table_names --> use engine.table_names()
table_names = engine.table_names()

# Print the table names
print(table_names)

# %%
# QUERY THE DATABASE IN PYTHON
# WORKFLOW OF SQL QUERYING
# - import packages and functions (sqlalchemy, pandas)
# - create the database engine --> create_engine('sqlite:///')
# - connect to the engine --> con = engine.connect()
# - query the database --> rs = con.execute("SELECT * FROM orders")
# - save query results to a DataFrame --> df = pd.DataFrame(rs.fetchall())
# - set the column names --> df.columns = rs.keys()
# - close the connection --> con.close()

# we can use the context manager to open and close the connect to engine
# with engine.connect() as con: --> case of forget to close the connection
#     rs = con.execute("SELECT OrderID, Order... FROM Orders") --> selected columns
#     df = pd.DataFrame(rs.fetchmany(size=5)) --> select only 5 rows
#     df.columns = rs.keys()

# Query the 'Chinook.sqlite'
# Import packages (sqlalchemy, pandas)
from sqlalchemy import create_engine
import pandas as pd

# Create database engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Connect to the engine: con
con = engine.connect()

# Query select all columns from Album table
rs = con.execute("SELECT * FROM Album")

# save query as DataFrame: df
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()
# Print out the head of df
print(df.head(0))
# %%
# open engine with context managerment
# Select columns 'LastName', 'Title' from 'Employee' store as rs1
# retrieve 3 records as df1
# using rs object, set the DataFrame's column names to the corresponding
# names of the table columns

# open engine with context management
with engine.connect() as con:
    rs1 = con.execute("SELECT LastName, Title FROM Employee")
    df1 = pd.DataFrame(rs1.fetchmany(3))
    # set name
    df1.columns = rs1.keys()

# Print the lens of the DataFrame
print(len(df1))
# Print the head of the df
print(df1.head())

# %%
# Select all records of the Employee table for which 'EmployeeId' >=6
with engine.connect() as con:
    rs2 = con.execute("SELECT * FROM Employee WHERE EmployeeId >=6")
    df2 = pd.DataFrame(rs2.fetchall())
    # set name
    df2.columns = rs2.keys()
# Print the head of df2
print(df2.head())

# %%
# Select all records of the Employee table and order in increasing order 
# by the column BirthDate

with engine.connect() as con:
    rs3 = con.execute("SELECT * FROM Employee ORDER BY BirthDate")
    df3 = pd.DataFrame(rs3.fetchall())
    # set name
    df3.columns = rs3.keys()
print(df3.head())

# %%
# RUN query direct from PYTHON with PANDAS
# df = pd.read_sql_query("QUERY...", engine)
# Select all records from the Album table and compare the results

df4 = pd.read_sql_query("SELECT * FROM Album", engine)
print(df4.head())
# Confirm 2 methods yield the same result
print(df.equals(df4))

# %%
# Build DataFrame that contains the rows of the Employee table for which
# the EmployeeId is >= 6 and ordering by BirthDate

df5 = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate", engine)

# Print head of df5
print(df5.head())
print(df5.shape)


# %%
#ADVANCED QUERYING: EXPLOITING TABLE RELATIONSHIPS
# - Join tables together
#     - INNER JOIN

# - Extract the Title along with the Name of the Artist. INNER JOIN on the ArtistID
# - Use context management

# Perform the query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.head())

# %%
# Assign variable 'df' the DataFrame of results from the following query:
# select all records from PlaylistTrack and Track based on TrackId where Milliseconds < 250000

df = pd.read_sql_query("SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000", engine)

print(df.head())
# %%
print(engine.table_names())

print(con.Album.columns.keys())
# %%
