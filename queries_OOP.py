from database_OOP import database_OOP
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

"""
Look up plugins that can visualise the data in a clean way.
"""

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


    def execute_second_command(self):
        server = 'databases2.spartaglobal.academy'
        database = 'Northwind'
        username = 'SA'
        password = 'Passw0rd2018'
        object = database_OOP(server, database, username, password)
        cursor = object.establish_connection()
        query_result = """SELECT AVG(sq1.[Time Taken To Ship Orders]) AS "Average Time Taken Per Month"
                            ,sq1.[Date Of Delivery] "Month Of Delivery"
                            FROM (SELECT (DATEDIFF(d,OrderDate,ShippedDate)) AS "Time Taken To Ship Orders"
                            ,FORMAT(o.OrderDate, 'yy-MM') AS "Date Of Delivery"
                            FROM Orders o) sq1
                            GROUP BY sq1.[Date Of Delivery]
                            ORDER BY sq1.[Date Of Delivery]"""
        rows = cursor.execute(query_result)
        time_taken_to_ship_orders = []
        average_time_taken_per_month = []
        for keys, values in rows:
            time_taken_to_ship_orders.append(keys)
            average_time_taken_per_month.append(values)
        # print(time_taken_to_ship_orders)
        # print(average_time_taken_per_month)
        df = pd.DataFrame()
        df["Time Taken To Ship Orders"] = time_taken_to_ship_orders
        df["Average Time Taken Per Month"] = average_time_taken_per_month
        pd.set_option("display.max_rows", len(time_taken_to_ship_orders))
        print(df.head(len(time_taken_to_ship_orders)))

        plt.plot(average_time_taken_per_month, time_taken_to_ship_orders)
        plt.show()








        """
        By returning the number of items in the list we can ensure the correct number of rows
        are printed in the df.head()
        """
        """
        Pandas can intialise tables or columns, tables are referred to as dataframes (df)
        """



