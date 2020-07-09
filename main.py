from database_OOP import database_OOP

"""
Find out how to encode the password in Python
"""
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'


object = database_OOP(server, database, username, password)

print(object.establish_connection())
object.create_cursor(connection)