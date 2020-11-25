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
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# %%
