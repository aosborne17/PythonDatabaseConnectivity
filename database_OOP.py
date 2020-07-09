import pyodbc

"""
This file is much better than the database connections file
because we have certain methods that are carrying out ONE function.

However, the other file has many functionalities all over the place
"""


class database_OOP:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    # this method is specifically for establishing a connection
    def establish_connection(self):
        connections = ('DRIVER={ODBC Driver 17 for SQL Server};'
                                     'SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        # return connections

        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection did not timeout")
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
            print("Connection Timed Out")
        except pyodbc.InterfaceError:
            print("Invalid connection to DB interface")
        else:
            return connection

    # This is specifically for creating the cursor
    def create_cursor(self, connection):
        cursor = connection.cursor()
        return connection.cursor

    # This method is strictly for executing SQL commands
    def execute_sql(self, sql_command, connection, user_input):
        pass

