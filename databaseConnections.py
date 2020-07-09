import pyodbc # This allows us to connect to the databases
import pandas as pd
import numpy as np

"""
pyodbc is a library that helps us connect to a database
"""

"""
We are trying to establish a connection and read data from
the database in the python console.
UI = user interface, this is the front end of development
"""

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connections.cursor()

print(connections)
print(cursor)


print("Printing query_result object:", query_result)

# this wil fetch on row from the database

rows = query_result.fetchone() # fetches row in order, so if you do it twice it would take the next row underneath
print(type(rows)) # will tell you the type 'pdobc.row'
print(rows[1]) # this would collect from the second column 'product name' in this case
               # remember index starts from 0 hency why we select the recond column

# fetchmany allows us to get multiple rows at a time
# note if we are on the second fetch, after this we would move to the 32nd position
rows = query_result.fetchmany(30)



