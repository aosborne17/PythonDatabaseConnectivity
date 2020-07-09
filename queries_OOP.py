from database_OOP import database_OOP
import pandas as pd
import numpy as np


class Check_queries:
    def __init__(self):
        pass

    def execute_commands(self):
        server = 'databases2.spartaglobal.academy'
        database = 'Northwind'
        username = 'SA'
        password = 'Passw0rd2018'
        object = database_OOP(server, database, username, password)
        cursor = object.establish_connection()
        query_result = 'SELECT CustomerID, CompanyName FROM Customers;'
        rows = cursor.execute(query_result)
        Customer_ID = []
        Company_Name = []
        for keys, values in rows:
            Customer_ID.append(keys)
            Company_Name.append(values)
        # print(Customer_ID)
        # print(Company_Name)
        df = pd.DataFrame()
        df["CustomerID"] = Customer_ID
        df["Company Name"] = Company_Name
        pd.set_option("display.max_rows", len(Customer_ID)) # Using pandas module, allows us to print all the rows in the columns
        print(df.head(len(Customer_ID)))   # returns the rows in the dataframe table, if left empty, 5 rows will be printed (from index 0 to 5)


        """
        By returning the number of items in the list we can ensure the correct number of rows
        are printed in the df.head()
        """
        """
        Pandas can intialise tables or columns, tables are referred to as dataframes (df)
        """



